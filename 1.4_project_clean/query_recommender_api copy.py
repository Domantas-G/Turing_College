import pandas as pd
from typing import List
from sqlalchemy import text
from database import engine, SessionLocal


class QueryRecommender_api:
    """
    API for Data Scientists to execute SQL queries on a MySQL Database in Python environment.
    And a Recommender engine that provides recommended titles to watch next based on imput titles.
    This API includes a recommender for a single or a list of titles.
    Saves that data and allows to publish it directly to the database table "Recommendations".

    This API contains Recommender and Query class, that is connected to MySQL server.


    Attributes:
      engine: sqlalchemy.Engine imported from database.py to connect to the database.
      session_factory: A factory for creating new Session objects, imported from database.py.
      data: Data fetched from a SELECT query.
      retrieved_data: Data fetched for recommendation purposes.
      outputs: The final recommendations stored in DataFrame format, used for uploading to database.

    Methods:
      read: Executes a SELECT query and returns the result as a DataFrame.
      write: Executes a write (INSERT, UPDATE, DELETE) or create query against the database.
      recommender_retrieve: Retrieves data required for the recommender and returns it as a DataFrame.
      recommend_title: Returns top 5 recommendations for a given title's id.
      recommend_titles: Returns top 5 recommendations for each title id in the list.
      recommender_send_data: Sends the outputs DataFrame to the 'recommendations' table in the MySQL database.
      turn_off_fk_check: Turns off foreign key checks in the MySQL database.
      turn_on_fk_check: Turns on foreign key checks in the MySQL database.
    """

    def __init__(self) -> None:
        self.engine = engine
        self.session_factory = SessionLocal
        self.data = None
        self.retrieved_data = None
        self.outputs = None

    def read(self, query: str) -> pd.DataFrame:
        """Executes a SELECT query and returns the result as a DataFrame."""
        query = query.strip()
        if not query.upper().startswith("SELECT"):
            raise ValueError("Not a SELECT statement")

        session = self.session_factory()
        try:
            result = session.execute(text(query))
            self.data = pd.DataFrame(result.fetchall(), columns=result.keys())
        finally:
            session.close()
        return self.data

    def write(self, query: str) -> None:
        """Executes a write (INSERT, UPDATE, DELETE) or create query against the database."""
        session = self.session_factory()
        try:
            session.execute(text(query))
            session.commit()
        except Exception as e:
            session.rollback()
            raise ValueError(f"An error occurred while executing query: {e}") from e
        finally:
            session.close()
        print(f"Successfully executed query: \n{query}")

    def recommender_retrieve(self) -> pd.DataFrame:
        """Retrieves data required for the recommender and returns it as a DataFrame."""
        retrieve_query = """SELECT 
                            t1.id,
                            t1.title,
                            t1.imdb_score,
                            t2.genre
                            FROM titles AS t1
                            LEFT JOIN title_genres AS t2
                            ON t1.id=t2.id"""

        session = self.session_factory()
        try:
            result = session.execute(text(retrieve_query))
            self.retrieved_data = pd.DataFrame(result.fetchall(), columns=result.keys())
        finally:
            session.close()
        return self.retrieved_data

    def recommend_title(self, input_id: List[str]) -> pd.DataFrame:
        """Returns top 5 recommendations for a given title's id."""
        if self.retrieved_data is None:
            raise ValueError(
                "Data not loaded. Use the 'recommender_retrieve' method to load data first."
            )

        self.retrieved_data.drop_duplicates(subset="id", keep="first", inplace=True)
        input_data = self.retrieved_data[self.retrieved_data["id"].isin(input_id)]
        input_genres = input_data["genre"].unique()

        recommendations = self.retrieved_data[
            self.retrieved_data["genre"].isin(input_genres)
            & (~self.retrieved_data["id"].isin(input_id))
        ]
        top_recommendations = recommendations.sort_values(
            by="imdb_score", ascending=False
        ).head(5)

        output_data = {
            "input_id": input_data["id"].values[0],
            "input_title": input_data["title"].values[0],
            "imdb_score": input_data["imdb_score"].values[0],
            "genre": input_data["genre"].values[0],
        }
        for i, rec_title in enumerate(top_recommendations["title"].values, start=1):
            output_data[f"rec_title_{i}"] = rec_title

        self.outputs = pd.DataFrame([output_data])
        return self.outputs

    def recommend_titles(self, input_ids: List[str]) -> pd.DataFrame:
        """Returns top 5 recommendations for each title id in the list."""
        if self.retrieved_data is None:
            raise ValueError(
                "Data not loaded. Use the 'recommender_retrieve' method to load data first."
            )

        self.retrieved_data.drop_duplicates(subset="id", keep="first", inplace=True)
        outputs = []
        for input_id in input_ids:
            input_data = self.retrieved_data[self.retrieved_data["id"] == input_id]
            input_genres = input_data["genre"].unique()
            recommendations = self.retrieved_data[
                self.retrieved_data["genre"].isin(input_genres)
                & ~self.retrieved_data["id"].isin([input_id])
            ]
            top_recommendations = recommendations.sort_values(
                by="imdb_score", ascending=False
            ).head(5)

            output_data = {
                "input_id": input_data["id"].values[0],
                "input_title": input_data["title"].values[0],
                "imdb_score": input_data["imdb_score"].values[0],
                "genre": input_data["genre"].values[0],
            }
            for i, rec_title in enumerate(top_recommendations["title"].values, start=1):
                output_data[f"rec_title_{i}"] = rec_title

            outputs.append(output_data)

        self.outputs = pd.DataFrame(outputs)
        return self.outputs

    def recommender_send_data(self) -> None:
        """Sends the outputs DataFrame to the 'recommendations' table in the MySQL database."""
        self.turn_off_fk_check()

        try:
            self.outputs.to_sql(
                name="recommendations", con=self.engine, if_exists="append", index=False
            )
            print("Data sent to MySQL database successfully.")
        except Exception as e:
            raise ValueError(
                f"An error occurred while loading data into recommendation into a table: {e}"
            ) from e
        finally:
            self.turn_on_fk_check()

    def turn_off_fk_check(self) -> None:
        """Turns off foreign key checks in the MySQL database."""
        with self.engine.connect() as conn:
            conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        print("Foreign key checks turned off.")

    def turn_on_fk_check(self) -> None:
        """Turns on foreign key checks in the MySQL database."""
        with self.engine.connect() as conn:
            conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        print("Foreign key checks turned on.")
