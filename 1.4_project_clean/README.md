# dgervi-DE1.4

# Author: Domantas Gervinskas

![netflix](https://filmschoolrejects.com/wp-content/uploads/2017/09/netflix-logo.jpg)

# Project Introduction: Netflix Data Warehouse, Database Query and Recommender APIs for analytics and data science

This project sets up a database and backend infrastructure for Netflix movies and series catalog, ensuring seamless data access and integration for both ad-hoc SQL queries by analysts and the simulation engine utilized by data scientists, including a recommender engine that they can deploy.
The goal is to import, clean, process and perform EDA on Netflix data, normalize it to 3NF, split it into smaller dataframes, and store them in a MySQL database. Finally API is create for data science team to read and write to/from database using SQL queries in Python environment, perform simulations and recommendations through recommenders and then write back to the database.

## Prerequisites / Requirements

- Python 3.11
- MySQL database

Install the prerequisite Python libraries from the provided `requirements.txt` file:

```
pip install -r requirements.txt
```

## Goals & Objectives

- Translate business and project requirements into data engineering tasks
- Evaluate and Select an RDBMS
- Import, clean and transform data
- Perform EDA to gain insights into the data.
- Data enrichment from best movies/shows tables.
- Normalize the data to 3NF to eliminate redundancy and ensure data integrity.
- Create MySQL database and tables directly from Python, with Primary and Foreign keys.
- Create an ERD showing relationships between tables.
- Populate MySQL database tables with data from panda Dataframes.
- Create users and split data access rights to
  - Read for data analysts (in Database application)
  - Read/Write for data scientists (in Python environment)
- Create and expose a Python API (or Web API) that can perform read/write SQL queries on a database.
- Build a demo recommender, showcase how it works
- Implement monitoring & logging

## Features

- Import and preprocess data using data classes and pandas.
- Data models and schemas defined in SQLAlchemy.
- Create, configure and setup a MySQL database from Python using data classes.
- Load data from from Python environment into the database.
- An API for reading/writing SQL queries on a MySQL database in Python.
- An API for recommending next titles to watch based on one or multiple titles.

# Deliveries

## Assumptions

- Data engineer is free to choose a database for the initial project, and it's best to choose the one they are familiar with the most. In real world a data engineer comes into a job and they work with the database that is used by the company or install the one that is chosen by data architech.
- Data Scientists generally work not on Prod database but on a replica or a loosely coupled database that that the same contents as Prod but can be restored from it. This allows for quick access and freedom to do and test hypotheses and models. As such the assumption is that as long as a person has access to an API, meaning they are working for a company and company provided access to an API, they should be allowed to execute queries not only for reading but also for deleting or creating tables, hence API does not restrict query parameters. Generally, it is not advised to have an open or exposed API to execute SQL queries against a database due to the risk of injection attacks.
- Data engineer is allowed to choose the level of database Normalization.

## Evaluate and select an RDBMS

After long evaluation of all available RDBMS, for this project MySQL database was chosen because it's secure, flexible, very easy to setup, user friendly, and the author of this project is more familiar with it than with the other RDBMS'.
Reasons for choosing MySQL database that work well with this project:

- It's free and open source, which is very good for experimental projects
- It's one of the oldest and most popular RBDMS
- Has mature code base and community support
- Good documentation
- High performance and reliability, handles concurrent users which is important for simulations that this project performs
- Integrates well with web applications
- Many tools and plugins available
- Visual aids for database design
- Integrated ERD creation and manipulation
- MySQL can run on any Operating System
  Good security - strong data encryption, SSL support, and user access privilege management
  ACID (Atomicity, Consistency, Isolation, Durability) properties guarantees that database transactions are processed reliably

Main RDBMS' that were in consideration:

- MySQL: a free and open-source.
- PostgreSQL: a free and open-source.
- Amazon Redshift: cloud based.
- DB2: cloud based.
- SQL Server: generally used by businesses.
- SQLite: a lightweight and embedded RDBMS that is self-contained and serverless.

## Import, clean and transform data

First step with data is always to check what kind of data we have and get initial understanding of the sources, formats, volume, missing values, and the like.
I begin with checking for missing values and find that:

For Titles:

- Seasons has 64.74% missing, as expected because it applies to series and shows, but not movies.
- Age_certification has 44.95% missing, which can mean that there is no age census.
- imdb_votes and imdb_score has 9.28% and 9.01% missing respectively, which means that some titles did not receive any votes or score, which does reflect reality as these are related and not all creations get recognition.
- imdb_id has 7.65% missing, meaning that there are titles that did not have or was not linked to an IMDB.
- title 0.02% missing with one title missing.
  For Credits:
- character has 12.47% values missing, which generally meant that the role of that person was a Director. Technically not missing, just not a character in a movie.

Then for both datasets following operations were performed:

- Duplicate rows removed
- Additionally for Titles removed duplicates for 'id' and 'imdb_id' as these indicate the same title being added twice.
- Removed brackets and quotes from columns that had list items in it (these are later split into separate values per row at Normalization stage)
- Missing values imputed to zero or None for most
- Except for Imdb score and votes which were set to median to keep data consistent.

## EDA (Exploratory Data Analysis)

The EDA was carried out to gain insights into the dataset. Various visualizations are generated to understand distributions, relationships, outliers present in the data. Specifically:

- Descriptive statistics checked:
  - The oldest title in the dataset is from 1945, newest is from 2022, mode 2019.
  - Average runtime is 84mins, distribution peaks at around 90-100 minutes, longest is 251min.
  - 75% of titles have 1 season or less, and maximum seasons for a title is 42.
  - Average imdb score is 6.5, maximum is 9.6.
  - Only 50% of titles have more than 2279 votes, which means that most title receive very little attention.
- There are non-alpha-numeric values in columns ['title', 'age_certification', 'genres', 'production_countries', 'imdb_score'], but in all cases it's something like ". , / -" etc.
- Top 5 best rated movies of all time, that are on Netflix, are:
  - David Attenborough: A Life on Our Planet
  - Chhota Bheem & Krishna in Mayanagari
  - C/o Kancharapalem
  - No Longer Kids
  - Inception
- Correlation Matrix
  - imdb_score and imdb_votes have a positive correlation, meaning that titles with higher ratings received more votes.
- Type analysis:
  - There are more Movies than Shows.
- Genre Analysis
  - Drama, comedy, and then far behind a third genre of action are the most common genres in the dataset.
  - Top 3 genres by average IMDB score are history, war and documentation.
  - Top 3 by average IMDB votes are western, followed far behind by war and scifi.
- Runtime analysis
  - No clear trend between runtimes and IMDB scores.
  - Movies have higher median runtime than TV shows.
- Production Country Analysis:
  - The US, India and the UK are the leading producers of movies and shows.
  - Titles from the United Kingdom have the highest average IMDb score among the top 10 production countries.
- Release Year Analysis:
  - The number of titles released per year has been on the rise since the 1980s.
  - Pre 1970 titles have higher average IMDb scores.
- Age Certification Analysis:
  - Most titles either lack an age certification or are classified as "TV-MA" or "TV-14".
  - Titles with a "G" certification have the highest average IMDb score.
- Top Actors/Directors:
  - Top actors and directors appear to be of Indian descent.
  - Top actors based on number of titles: Shah Rukh Khan, Anupam Kher, and Kareena Kapoor Khan.
  - Top directors based on number of titles: Raúl Campos, Jan Suter, and Jay Karas.
- Outliers were checked, but no winsorization or outlier removal performed because this data accurately reflect each title's case.
- Generate Word Cloud for graphical investigation of most common themes.

## Normalize the data to 3NF

Third Normal Form (3NF) usually is sufficient for most applications, reduces redundancy, ensuring data integrity and does not create managerial overhead.
For this case the following action were performed to normalize the data:

- Created titles_df with title related data only
- Titles type that contains id, title type and factorized unique id for each different title type
- Titles genre that contains id, split out genres into individual cases and factorized unique id for each different genre
- Titles country that contains id, split out countries into individual cases and factorized unique id for each different country
- Credits that contain id, serialized credit id, person id, role and character
- Credits persons that contain only person id and person name

## Data Enrichment

In addition to Titles and Credits information, there is data about best movies/shows ever and by year provided alongside.
This data is not directly included on the original datasets and thus can be used to enrich the data with flags to denote when a movie/show has been awarded a title of being best ever or best of the year.
The process is as follows:

- Import the datasets
- Inner merge them on identical fields to get only the intersection
- Check lengths between merged and imported datasets to see if they match
- Resolve the single conflict that occurs with duplicate title
- Check if there are titles in new datasets that titles that don't have a match in Titles. Titles in the new datasets are consistent with the Titles dataset.
- Create a Flag in the original Titles dataset for each of the merged datasets, when a title is present in one of those datasets.

## Create MySQL database and tables

Then once datasets are ready it's time to create a MySQL database.
Starting point is designing the database schema, this involves defining entities, attributes, and their relationships. ERD as defined in the configuration:
![ERD_Diagram](res.ERD_img.png)
The factual definition is done in Python, using SQLAlchemy library in `models.py`.
It uses declarative_base() Base class from `database.py` that defines the connection to the MySQL database itself.
Then execute code in order to create MySQL database and tables directly from Python, with Primary and Foreign keys.

Then from MySQL using UI create an ERD showing relationships between tables.

## Populate MySQL database tables with data from panda Dataframes.

For data ingestion I created a Python class called database_loader that instantiates connection, create a database and to directly upload data to the database from pandas datafranes. Simply call the following functions in order to:

- create_engine: to create an engine for database connection predefined in settings file.
- create_database: to create a database with a name predefined in settings file.
- create_all: Create all tables from SQLAlchemy Base class.
- turn_off_fk_check: Turn off foreign key checking, to avoid validation error.
- send_data: Send dataframe into existing MySQL database table.
- turn_on_fk_check: Turn back on foreign key checking.

## Create a MySQL read rights user for data analysts

To grand access to data analysts to execute SQL read queries on the database to perform analysis and gain insights about the data, best option is to create a new user for them, following the process:

- Open Terminal or MySQL CLI/Workbench
- Login as administrator
  `mysql -u root -p`
- Create a new user with password and privileges:

```
CREATE USER 'data_analyst'@'localhost' IDENTIFIED BY 'random_pass';
GRANT SELECT ON netflix_movies.* TO 'data_analyst'@'localhost';
FLUSH PRIVILEGES;
```

Now this analyst can login directly in MySQL or in any other CLI application and execute SQL SELECT statements, but they won't have write or modify access to the data, as requested.

## Read/Write for data scientists

For data scientists there is a need to be able to execute Read and Write SQL queries directly in Python environment, this requires to create and expose a Python API (or Web API).

API requirements:

- Has to be available in Python.
- Ability to perform read and write operations.
- Ability to understand and execute SQL queries directly in Python on MySQL database.
- Error handling for errors, and to debug code.
- In case Writing data fails to roll back to pre-execution state to avoid corrupting the database state or data.
- Ensure both SQL and Python interactions are stable.
- Assumption is that Data scientists work on a database replica and not Production version, hence write access does not carry as much risk.
- Implemented monitoring & logging for all write operations to monitor and audit changes made to the database.

For this reason I have built a query_recommender_api keeping all these requirements in mind. The API allows anyone with the access to it to perform read/write SQL queries directly on a database straight from Python.

To use it import query_recommender_api class from query_recommender_api and then perform methods:

- read(): Executes a SELECT query and returns the result as a DataFrame.
- write(): Executes a write (INSERT, UPDATE, DELETE) or create query against the database.

Example use:

```
from query_recommender_api import QueryRecommender_api
recommender_api = QueryRecommender_api()
recommender_api.recommender_retrieve()

query = "SELECT * FROM titles"
recommender_api.read(query)
write_query = "CREATE TABLE demo_table (demo_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL)"
recommender_api.write(write_query)
```

## Build a demo recommender, showcase how it works

Built a demo recommender engine integrated into the query_recommender_api that allows for direct inteaction with data in Python.
How it works is you first have to retrieve the data from the database using recommender_retrieve() method that executes a specific query in connected MySQL database and then stores this data inside the class instance. This method ensures the simulation engine can easily fetch required data via the API.

Then you can input a title id into recommend_title() method and it will provide 5 recommendations for that title based on the genre of the original title.
If you have more than 1 title id on which you'd like to receive recommendation then there is an option to use recommend_titles() by passing a list of ids as an argument. This will prove output in the same format as previous method. Both methods save the output data inside the instance.
Last method is used to send this saved recommendation data directly into the database. To perform it you have to call recommender_send_data() that sends the recommendations' output DataFrame to the 'recommendations' table in the MySQL database. These methods ensure that the simulation engine has an easy way to write predictions and recommendations back to the database via the API.

Usage same as for read/write API:

- recommender_retrieve(): Retrieves data required for the recommender and returns it as a DataFrame.
- recommend_title(): Returns top 5 recommendations for a given title's id.
- recommend_titles(): Returns top 5 recommendations for each title id in the list.
- recommender_send_data(): Sends the outputs DataFrame to the 'recommendations' table in the MySQL database.

Example use:

```
recommender_api = QueryRecommender_api()
recommender_api.recommender_retrieve()
recommender_api.recommend_title(input_id=['tm1000185', 'ts99814'])
recommender_api.recommender_send_data()
recommender_api.recommend_titles(['tm1000037', 'tm1000147'])
recommender_api.recommender_send_data()
```

# Usage

1. Clone the repository.

```
git clone https://github.com/TuringCollegeSubmissions/dgervi-DE1.2.git
cd dgervi-DE1.4/
```

2. Update your settings file to contains information about your database connection.

3. Create a database "netflix_movies". (Current implementation necessitates the database to be created when instantiating the `database.py`, though it can be turned off and then database can be created directly from Python with `database_loader.py`)

4. Run the Python script to import, preprocess, normalize the data.

5. Run `data_analysis.ipynb` notebook to perform and view the EDA results.

6. Create MySQL database tables and Primay/Foreign key relationships from Python using `models.Base.metadata.create_all(bind=engine)` to create all tables in the database based on ERD configuration.

7. Populate database tables with data from panda Dataframes using `database_loader.send_data()` method.

8. Perform queries for Reading and Writing SQL queries through API `query_recommender_api.py`.

9. Perform demo recommendations for random titles using `query_recommender_api.py` methods, and send the data to database.

10. Check if the data is in the database.

## Suggestions for Improvement

- Update the classess to have only 1 of them instantiating database connection instead of 2. I have not yet decided which I like more.
- Update recommender to take into account not only genres for recommendation, but also imdb scores, actors, directors, production country, etc.
- Add Pydantic for data validation.
- Use FastAPI for database ingestion, retrieval and recommendation (currently did not manage to get all of this to work and dropped it due to time constraints).
- GraphQL would have been amazing for this project, would help to see clusters of related actors and directors, countries, decades, etc.
- Foreign Key checks fail on Credits table, but if inserting the same data manually in MySQL it succeeds. For this to work I had to turn off FK checks before data ingestion.
