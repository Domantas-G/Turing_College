import os
import sys

"""Adding absolute path for to be able to import config"""
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from config.settings import (
    DATABASE_DRIVER,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
)

import mysql.connector
from sqlalchemy import create_engine, text
import setup.models as models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseLoader:
    """
    Database Creation and Insertion API

    This API contains DatabaseLoader class, that connects to MySQL server using a configuration file,
    creates a database and allows for pushing data from Pandas dataframe to MySQL server tables.

    Attributes:
        engine: SQLAlchemy Engine for database connection.
        session: SQLAlchemy Session for database interactions.
        config: configuration the INI file.

    Methods:
        create_engine: Create an engine for database connection.
        create_database: Creat a database.
        create_all: Create all tables from SQLAlchemy Base class.
        send_data: Send dataframe into existing MySQL database table.
        turn_off_fk_check: Turn off foreign key checking.
        turn_on_fk_check: Turn on foreign key checking.
    """

    def __init__(self):
        self.engine = None
        self.session = None

    def create_engine(self):
        self.engine = create_engine(
            f"{DATABASE_DRIVER}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/"
        )

    def create_engine_with_db(self):
        self.engine = create_engine(
            f"{DATABASE_DRIVER}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        )

    def delete_database(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(f"DROP DATABASE IF EXISTS {DATABASE_NAME}"))
        except Exception as e:
            print(f"An error occurred while deleting database {e}")
        print("Old database deleted.")

    def create_database(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))
                print("Database created.")
        except Exception as e:
            print(f"An error occurred while creating database {e}")
        # finally:
        #     with self.engine.connect() as conn:
        #         conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))

        # Update the engine to use the new database
        self.engine = create_engine(
            f"{DATABASE_DRIVER}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        )
        print("Engine updated.")

    def create_tables(self):
        # Create all tables in MySQL database from models.py definitions.
        # Base.metadata.create_all(self.engine)
        models.Base.metadata.create_all(self.engine)
        print("Tables created.")

    # def session(self):
    #     try:
    #         sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    #     except Exception as e:
    #         raise Exception("Error occurred: ", str(e))

    def add_cities(self, cities):
        """Adds a list of cities to the database.
        Skips cities that already exist in the table.

        Args:
            cities (list): A list of city names to be added.
        """
        # Ensure the engine is created
        if not self.engine:
            self.create_engine_with_db()

        # Create a session
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            for city_name in cities:
                # Check if city already exists
                existing_city = (
                    session.query(models.City)
                    .filter(models.City.city_name == city_name)
                    .first()
                )
                if not existing_city:
                    # Add new city
                    new_city = models.City(city_name=city_name)
                    session.add(new_city)
                    print(f"Added city: {city_name}")
                else:
                    print(f"City already exists: {city_name}")

            # Commit the session
            session.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def remove_cities(self, cities):
        """Removes a list of cities from the database.

        Args:
            cities (list): A list of city names to be removed.
        """
        # Ensure the engine is created
        if not self.engine:
            self.create_engine_with_db()

        # Create a session
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            for city_name in cities:
                # Check if city exists
                existing_city = (
                    session.query(models.City)
                    .filter(models.City.city_name == city_name)
                    .first()
                )
                if existing_city:
                    # Remove city
                    session.delete(existing_city)
                    print(f"Removed city: {city_name}")
                else:
                    print(f"City does not exist: {city_name}")

            # Commit the session
            session.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def send_data(self, df, db_table):
        """Sends a DataFrame to a specific table in the MySQL database.
        Usage: db_loader.send_data(titles_df, 'titles')"""
        try:
            df.to_sql(name=db_table, con=self.engine, if_exists="append", index=False)
        except Exception as e:
            raise Exception("Error occurred: ", str(e))

    def turn_off_fk_check(self):
        """Turns off foreign key checks in the MySQL database."""
        with self.engine.connect() as conn:
            conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        print("Foreign key checks turned off.")

    def turn_on_fk_check(self):
        """Turns on foreign key checks in the MySQL database."""
        with self.engine.connect() as conn:
            conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        print("Foreign key checks turned on.")
