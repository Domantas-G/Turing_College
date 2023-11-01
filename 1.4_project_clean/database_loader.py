import os
from settings import (
    DATABASE_DRIVER,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
)

import mysql.connector
from sqlalchemy import create_engine, text
import models


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

    def create_database(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))
        except Exception as e:
            print(f"An error occurred while loading data into {e}")
        # finally:
        #     with self.engine.connect() as conn:
        #         conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))

        # Update the engine to use the new database
        self.engine = create_engine(
            f"{DATABASE_DRIVER}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        )
        print("Engine updated.")

    def create_all(self):
        # Create all tables in MySQL database from models.py definitions.
        # Base.metadata.create_all(self.engine)
        models.Base.metadata.create_all(self.engine)

    def send_data(self, df, db_table):
        """Sends a DataFrame to a specific table in the MySQL database.
        Usage: db_loader.send_data(titles_df, 'titles')"""
        try:
            df.to_sql(name=db_table, con=self.engine, if_exists="append", index=False)
        except Exception as e:
            raise ValueError(
                f"An error occurred while loading data into {db_table}"
            ) from e

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
