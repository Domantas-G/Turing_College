# dgervi-DE1.2

# Author: Domantas Gervinskas

![Bookstore](https://uniacco.com/blog/wp-content/uploads/2020/03/DARYY1.jpg)

## Project Introduction

This project revolves around the comprehensive dataset of 52,478 books listed in GoodReads' "Best Books Ever" collection. The dataset offers diverse information for each book, ranging from ratings, genres, awards, to the characters that appear in each story. The overarching goal is to utilize this data to aid in training a custom-built proprietary large language model (akin to GPT-3) for generating fictional books.

## Prerequisites / Requirements

Before diving into the project, ensure you have the following prerequisites installed:

- Python 3.9+
- Required Python libraries:
  - pandas
  - numpy
  - sqlalchemy
  - mysql-connector-python
  - matplotlib
  - seaborn
  - chardet
  - dateutil
  - typing
- A MySQL server setup.

To install the prerequisite Python libraries, you can use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Goals

1. Load the GoodReads Best Books dataset into Python and perform an initial analysis.
2. Normalize the data up to the 2NF (Second Normal Form).
3. Create a MySQL database and establish the necessary tables directly from Python.

- ERD as defined in the configuration:
  ![ERD_Diagram](ERD_img.png)

4. Upload the data to the MySQL server using Python.

## Exploratory Data Analysis (EDA)

The EDA was carried out to gain insights into the dataset. Various visualizations were generated to understand distributions, relationships, and outliers present in the data. Specifically:

- Distribution of ratings and ratings count was visualized.
- Outliers were detected and handled using winsorization.
- The dataset was cleaned to remove unwanted characters, handle missing values, and drop duplicates.

## Features

1. **Encoding Identification**: The code initiates an attempt to detect the character encoding of the dataset using the `chardet` library. However, due to the diverse nature and size of the dataset, there are instances where the automatic detection was not successful. Therefore it was assumed the dataset is in 'UTF-8' encoding, which is a common encoding.

2. **Data Loading & Preprocessing**: The code is equipped to efficiently load and preprocess dataset. This includes:

   - Detecting and handling various character encodings.
   - Parsing and cleaning date formats.
   - Handling missing values and standardizing text data.
   - Unnesting lists and multiple value cases.

3. **Exploratory Data Analysis (EDA)**: Comprehensive exploratory data analysis is integrated into the code, offering visualizations and insights such as:
   - Distribution visualizations of numerical columns like ratings and page counts.
   - Outlier detection and mitigation using winsorization.
   - Analysis of categorical columns to identify data quality issues.
4. **Normalization**: The code systematically breaks down the data to achieve the Second Normal Form (2NF). This involves:

   - Splitting multi-valued columns into separate tables.
   - Creating unique identifiers for new tables.
   - Ensuring data integrity across tables.

5. **MySQL Integration**: Seamless integration with MySQL databases, allowing users to:
   - Create new databases and tables directly from Python.
   - Upload the processed and normalized data to MySQL tables.
   - Execute SQL queries from within the Jupyter notebook using SQLMagic.
6. **Dynamic Table Creation**: A notable feature of the code is its ability to dynamically create ORM classes based on the structure of the pandas DataFrame. This ensures flexibility and scalability for different datasets or schema changes.

7. **Views in MySQL**: The code offers functionality to create consolidated views in the MySQL database, allowing for easier querying of joined tables.

8. **Custom Utility Functions**: A collection of utility functions is available to handle common data manipulation and analysis tasks, making the code modular and reusable (stored in `functions_all.py`).

---

With these features, the code provides a robust toolkit for analyzing, processing, and integrating the GoodReads Best Books dataset into a MySQL database.

## Usage Steps

1. Clone the repository to your local machine.

```
git clone https://github.com/TuringCollegeSubmissions/dgervi-DE1.3.git
cd dgervi-DE1.3/
```

2. Ensure you have all the prerequisites installed.
3. Modify the `DATABASE_URL` in the Jupyter Notebook to connect to your MySQL server.
4. Run the Jupyter Notebook (`1.3_project.ipynb`).
5. The notebook will guide you through the steps of loading, analyzing, and storing the data in a MySQL database.

- Performs EDA and data cleaning.
- Visualize key information.
- Import, preprocess, normalize the data, split into smaller tables.
- Login to the MySQL database from Python.

```
  import db_config
```

- Create MySQL database tables and Primay and Foreign key relationships from Python.
- Populate database tables with data from panda Dataframes.
