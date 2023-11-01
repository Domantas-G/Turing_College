"""
Database Creation and Insertion API

This API contains DatabaseLoader class, that connects to MySQL server using a configuration file, 
creates a database and allows for pushing data from Pandas dataframe to MySQL server tables.
"""

from configparser import ConfigParser, NoSectionError, NoOptionError
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, text
import mysql.connector

from sqlalchemy import (
    Boolean,
    BigInteger,
    Column,
    create_engine,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    text,
)
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.schema import CreateTable

Base = declarative_base()


class DatabaseLoader:
    """
    A utility class for connecting to a MySQL database using configuration details.

    This class provides methods for loading database configuration from an INI file,
    establishing a connection to the MySQL database, and closing the database session.

    Attributes:
        engine: SQLAlchemy Engine object for database connection.
        session: SQLAlchemy Session object for database interactions.
        config: Parsed configuration from the INI file.

    Methods:
        load_config(): Load database configuration from an INI file.
        connect(): Connect to the MySQL database using configuration details.
        close(): Close the database session if it's open.

    """

    def __init__(self):
        self.engine = None
        self.session = None
        self.config = self.load_config()

        # if self.config:
        # self.connect()

    def load_config(self):
        """
        Load database configuration from an INI file.

        Returns: Parsed configuration.
        """
        # config_path = "../Config.ini"
        config_path = "config.ini"

        if not os.path.exists(config_path):
            print(f"Error: Configuration file {config_path} not found.")
            return None

        config = ConfigParser()
        config.read(config_path)

        # Check for required sections and keys
        try:
            user = config.get("mysql_netflix", "user")
            password = config.get("mysql_netflix", "password")
            host = config.get("mysql_netflix", "host")
            port = config.get("mysql_netflix", "port")
            database = config.get("mysql_netflix", "database")
        except (NoSectionError, NoOptionError) as exc:
            raise (f"Error reading configuration: {exc}") from exc

        return {section: dict(config[section]) for section in config.sections()}

    def create_engine(self):
        db_config = self.config["mysql_netflix"]
        self.engine = create_engine(
            f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/"
            # self.engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/")
        )

    def create_database(self):
        db_config = self.config["mysql_netflix"]
        with self.engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}"))

        # Update the engine to use the new database
        self.engine = create_engine(
            f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )

    # def connect(self):
    #     """
    #     Connect to the MySQL database using configuration details.
    #     """
    #     db_config = self.config["mysql_netflix"]

    #     connection_string = (
    #         f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@"
    #         f"{db_config['host']}/{db_config['database']}"
    #     )

    #     try:
    #         self.engine = create_engine(connection_string, echo=True)
    #         session = sessionmaker(bind=self.engine)
    #         self.session = session()
    #     except SQLAlchemyError as sql_er:
    #         raise (f"Error connecting to the database: {sql_er}") from sql_er

    # def close(self):
    #     """
    #     Close the database session if it's open.
    #     """
    #     if self.session:
    #         self.session.close()

    def create_all(self):
        # Create all tables in MySQL database.
        Base.metadata.create_all(self.engine)

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
