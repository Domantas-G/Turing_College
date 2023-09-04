import pandas as pd
import numpy as np
import re
import chardet
import ast
from typing import Optional, Union, Tuple, Dict, Any, List
from dateutil.parser import parse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import (
    create_engine,
    text,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    BigInteger,
    DateTime,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def detect_encoding(file_path: str) -> str:
    """
    Detect the character encoding of a given file.

    Args:
        file_path (str): The path to the file for which encoding needs to be detected.

    Returns:
        str: The detected encoding of the file.
    """
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
        return result["encoding"]


def split_and_get_first(input_string: str) -> str:
    """
    Split the input string on "." or "-" and extract the first part.
    If neither "." nor "-" is present, return the input string as it is.

    Args:
        input_string (str): Input string to be split.

    Returns:
        str: The first part of the split string or the original string if no split condition is met.
    """
    if "." in input_string:
        return input_string.split(".")[0]
    elif "-" in input_string:
        return input_string.split("-")[0]
    else:
        return input_string


def convert_string_to_list(x: str) -> list:
    """
    Convert a string representation of a list to an actual list.

    Args:
        x (str): String representation of a list.

    Returns:
        list: Actual list converted from the string representation.
    """
    if isinstance(x, str):
        return ast.literal_eval(x)
    return x


def standardize_date_format(date_str: str) -> Optional[Union[str, pd.Timestamp]]:
    """
    Convert various date string formats into a standard format.

    Args:
        date_str (str): The input date string to be standardized.

    Returns:
        Optional[Union[str, pd.Timestamp]]: The standardized date format
        or None if the date can't be parsed.
    """
    try:
        parsed_date = parse(date_str, fuzzy=True).date()

        if parsed_date.year > 2018:
            parsed_date = parsed_date.replace(year=parsed_date.year - 100)

        return parsed_date
    except:
        return None


def df_to_lowercase(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all string values in the dataframe to lowercase.

    Args:
        df (pd.DataFrame): The input dataframe whose string values need
        to be converted to lowercase.

    Returns:
        pd.DataFrame: DataFrame with all string values converted to lowercase.
    """
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.lower()
    return df


def analyze_categorical_column(
    dataframe: pd.DataFrame, column_name: str
) -> Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame]:
    """Analyze a categorical column of a given DataFrame.

    Args:
        dataframe (pd.DataFrame): Input dataframe containing the column to be analyzed.
        column_name (str): Name of the categorical column to analyze.

    Returns:
        Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame]: A tuple containing
        analysis results as a dictionary and
        dataframes with the shortest and longest values.
    """

    analysis_results = {}

    if column_name not in dataframe.columns:
        return f"The column '{column_name}' does not exist in the DataFrame."

    analysis_results["missing_values"] = dataframe[column_name].isnull().sum()
    analysis_results["unique_values"] = dataframe[column_name].nunique()
    analysis_results["total_values"] = dataframe[column_name].count()
    analysis_results["duplicated_values"] = dataframe[column_name].duplicated().sum()
    analysis_results["values_with_whitespace"] = (
        dataframe[column_name].str.strip().ne(dataframe[column_name]).sum()
    )
    analysis_results["values_with_unusual_chars"] = (
        dataframe[column_name]
        .apply(lambda x: any(ord(char) < 32 or ord(char) > 126 for char in str(x)))
        .sum()
    )

    value_lengths = dataframe[column_name].str.len()
    analysis_results["shortest_value_length"] = value_lengths.min()
    analysis_results["longest_value_length"] = value_lengths.max()
    analysis_results["average_value_length"] = value_lengths.mean()

    shortest_value = dataframe[
        dataframe[column_name].str.len() == analysis_results["shortest_value_length"]
    ]
    longest_value = dataframe[
        dataframe[column_name].str.len() == analysis_results["longest_value_length"]
    ]

    return analysis_results, shortest_value, longest_value


def extract_authors(author_str: str, non_authors: List[str]) -> str:
    """Extract main authors from the author string while excluding certain roles.

    Args:
        author_str (str): String containing author names and roles.
        non_authors (List[str]): List of roles that should be excluded from the result.

    Returns:
        str: Author names without roles.
    """
    names = [name.strip() for name in author_str.split(",")]
    authors = [
        re.sub(r"\((goodreads author|author)\)", "", name).strip()
        for name in names
        if not any(f"({role})" in name for role in non_authors)
    ]

    return ", ".join(authors)


def remove_brackets_content(s: str) -> str:
    """Remove content within brackets from a string.

    Args:
        s (str): Input string.

    Returns:
        str: String without content within brackets.
    """
    return re.sub(r"\(.*?\)", "", s).strip()


def most_common_lang(lang_str: str, language_rank: List[str]) -> str:
    """Get the most common language from a semicolon-separated list.

    Args:
        lang_str (str): String containing languages separated by semicolons.
        language_rank (List[str]): List of languages ranked by frequency.

    Returns:
        str: Most common language from the list based on provided ranking.
    """
    languages = [lang.strip() for lang in str(lang_str).split(";")]
    matched_language = next(
        (lang for lang in language_rank if lang in languages), languages[0]
    )

    return matched_language


def impute_missing_values(df):
    """
    Impute missing values in the dataframe.
    For columns of type int and float, impute with median.
    For columns of type object (strings), impute with mode.

    Parameters:
    - df: pandas DataFrame to be imputed

    Returns:
    - Imputed pandas DataFrame
    """

    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col].fillna(df[col].median(), inplace=True)
        elif df[col].dtype == "object":
            df[col].fillna("unknown", inplace=True)
    return df


def winsorize(
    df: pd.DataFrame,
    column: str,
    lower_quantile: float = 0.05,
    upper_quantile: float = 0.95,
) -> pd.DataFrame:
    """Apply winsorization to convert outliers into less extreme values.

    Args:
        df (pd.DataFrame): Input dataframe.
        column (str): Column name to apply the winsorization.
        lower_quantile (float, optional): Lower quantile. Defaults to 0.05.
        upper_quantile (float, optional): Upper quantile. Defaults to 0.95.

    Returns:
        pd.DataFrame: Dataframe with winsorized column.
    """
    lower_limit = round(df[column].quantile(lower_quantile))
    upper_limit = round(df[column].quantile(upper_quantile))
    df[column] = df[column].clip(lower=lower_limit, upper=upper_limit)
    return df


def outliers_numerical_cols(df: pd.DataFrame) -> None:
    """Visualize outliers in numerical columns using boxplots.

    Args:
        df (pd.DataFrame): Input dataframe.
    """
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns
    num_cols = 3
    num_rows = (len(numerical_columns) + 2) // num_cols

    plt.figure(figsize=(15, 5 * num_rows))
    for i, col in enumerate(numerical_columns, start=1):
        plt.subplot(num_rows, num_cols, i)
        sns.boxplot(x=df[col].dropna())
        plt.title(col)

    plt.tight_layout()
    plt.show()


def distribution_numerical_cols(df: pd.DataFrame, kde: bool = True) -> None:
    """Visualize distribution of numerical columns using histograms.

    Args:
        df (pd.DataFrame): Input dataframe.
        kde (bool, optional): Whether to plot a KDE (Kernel Density Estimation). Defaults to True.
    """
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns
    num_cols = 3
    num_rows = (len(numerical_columns) + 2) // num_cols

    plt.figure(figsize=(15, 5 * num_rows))
    for i, col in enumerate(numerical_columns, start=1):
        try:
            plt.subplot(num_rows, num_cols, i)
            sns.histplot(df[col], bins=30, kde=kde)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
        except:
            continue

    plt.tight_layout()
    plt.show()


def outlier_cols(column_data: pd.Series) -> bool:
    """Check if a column has outliers using IQR.

    Args:
        column_data (pd.Series): Column data to check.

    Returns:
        bool: True if outliers exist, False otherwise.
    """
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((column_data < lower_bound) | (column_data > upper_bound)).any()


def explode_column_to_table_no_na_drops(
    df: pd.DataFrame, column_name: str, new_column_name: str
) -> pd.DataFrame:
    """Explode a column that contains lists or arrays into separate rows in a new DataFrame.

    Args:
        df (pd.DataFrame): Input dataframe.
        column_name (str): Name of the column to be exploded.
        new_column_name (str): Name for the new column after exploding.

    Returns:
        pd.DataFrame: A new dataframe with exploded values from the specified column.
    """
    new_df = df[["bookId", column_name]].copy()

    new_df[column_name] = new_df[column_name].str.split(",")
    new_df = (
        new_df.explode(column_name)
        .reset_index(drop=True)
        .replace(r"[^0-9a-zA-Z ]", "", regex=True)
    )

    new_df.columns = ["bookId", new_column_name]
    new_df[new_column_name] = new_df[new_column_name].str.strip()
    new_df = new_df[new_df[new_column_name] != ""]

    df.drop(column_name, axis=1, inplace=True)

    return new_df


def explode_column_to_table(
    df: pd.DataFrame, column_name: str, new_column_name: str
) -> pd.DataFrame:
    """Explode a column that contains lists or arrays into separate rows in a new DataFrame.

    Args:
        df (pd.DataFrame): Input dataframe.
        column_name (str): Name of the column to be exploded.
        new_column_name (str): Name for the new column after exploding.

    Returns:
        pd.DataFrame: A new dataframe with exploded values from the specified column.
    """
    new_df = df[["bookId", column_name]].copy()

    new_df[column_name] = new_df[column_name].str.split(",")
    new_df = (
        new_df.explode(column_name)
        .reset_index(drop=True)
        .replace(r"[^0-9a-zA-Z ]", "", regex=True)
    )

    new_df.columns = ["bookId", new_column_name]
    new_df[new_column_name] = new_df[new_column_name].str.strip()
    new_df = new_df[new_df[new_column_name] != ""]

    new_df.dropna(subset=[new_column_name], inplace=True)

    new_df.drop_duplicates(inplace=True)

    df.drop(column_name, axis=1, inplace=True)

    return new_df


def mysql_class_from_df_pk(
    df: pd.DataFrame, tablename: str, pk_key: str = "bookId"
) -> type:
    """Create a SQLAlchemy class with a primary key for DataFrame.

    Parameters:
    - df (pd.DataFrame): The input dataframe.
    - tablename (str): Desired table name for the SQLAlchemy class.
    - pk_key (str, optional): Name of the primary key column. Default is "bookId".

    Returns:
    - type: SQLAlchemy ORM class.
    """

    type_mapping = {
        "int64": BigInteger,
        "Int64": BigInteger,
        "float64": Float,
        "object": String(300),
        "string": String(300),
        "bool": Boolean,
        "boolean": Boolean,
        "datetime64[ns]": DateTime,
    }

    attrs = {
        "__tablename__": tablename,
        "__table_args__": {"extend_existing": True},
    }

    for col, dtype in df.dtypes.items():
        if col == pk_key:
            attrs[col] = Column(
                type_mapping[str(dtype)], primary_key=True, autoincrement=True
            )
        else:
            attrs[col] = Column(type_mapping[str(dtype)])

    return type(tablename, (Base,), attrs)


def mysql_class_from_df_fk(
    df: pd.DataFrame, table_name: str, secondary_pk_col: str
) -> type:
    """Dynamically create an ORM class with a primary and foreign keys
    based on a given pandas DataFrame.

    Parameters:
    - df (pd.DataFrame): The input dataframe.
    - table_name (str): Desired table name for the SQLAlchemy class.
    - secondary_pk_col (str): The secondary column name for the composite primary key.

    Returns:
    - type: SQLAlchemy ORM class.
    """

    type_mapping = {
        "int64": BigInteger,
        "Int64": BigInteger,
        "float64": Float,
        "object": String(300),
        "string": String(300),
        "bool": Boolean,
        "boolean": Boolean,
        "datetime64[ns]": DateTime,
    }

    attributes = {
        "__tablename__": table_name,
        "__table_args__": (
            PrimaryKeyConstraint("bookId", secondary_pk_col),
            {"extend_existing": True},
        ),
        "bookId": Column(BigInteger, ForeignKey("books.bookId")),
    }

    for column, dtype in df.dtypes.items():
        if column != "bookId":
            attributes[column] = Column(type_mapping[str(dtype)])

    new_class = type(table_name, (Base,), attributes)
    return new_class


def mysql_class_from_df_fk_single_pk(df: pd.DataFrame, table_name: str) -> type:
    """Dynamically create an ORM class with a foreign key based on a given pandas DataFrame.

    Parameters:
    - df (pd.DataFrame): The input dataframe.
    - table_name (str): Desired table name for the SQLAlchemy class.
    - secondary_pk_col (str): The secondary column name for the composite primary key.

    Returns:
    - type: SQLAlchemy ORM class.
    """

    type_mapping = {
        "int64": BigInteger,
        "Int64": BigInteger,
        "float64": Float,
        "object": String(300),
        "string": String(300),
        "bool": Boolean,
        "boolean": Boolean,
        "datetime64[ns]": DateTime,
    }

    attributes = {
        "__tablename__": table_name,
        "__table_args__": {"extend_existing": True},
        "bookId": Column(BigInteger, ForeignKey("books.bookId")),
    }

    primary_key_name = table_name + "Id"
    attributes[primary_key_name] = Column(Integer, primary_key=True, autoincrement=True)

    for column, dtype in df.dtypes.items():
        if column not in [
            "bookId",
            primary_key_name,
        ]:
            attributes[column] = Column(type_mapping[str(dtype)])

    new_class = type(table_name, (Base,), attributes)
    return new_class


def factorize_id(df: pd.DataFrame, *args, id_field: str) -> pd.DataFrame:
    """
    Create a unique serialized integer value for each unique combination of
    specified columns using factorize.

    Args:
        df (pd.DataFrame): Input dataframe.
        *args: Columns to be used for unique combinations.
        id_field (str): Name of the new ID field.

    Returns:
        pd.DataFrame: DataFrame with a new ID field.
    """

    combined = df[list(args)].astype(str).agg("_".join, axis=1)

    df[id_field] = pd.factorize(combined)[0]

    return df


def serialize_id(df: pd.DataFrame, *args, id_field: str) -> pd.DataFrame:
    """
    Create a unique serialized integer value for each unique combination of
    specified columns.

    Args:
        df (pd.DataFrame): Input dataframe.
        *args: Columns to be used for unique combinations.
        id_field (str): Name of the new ID field.

    Returns:
        pd.DataFrame: DataFrame with a new ID field.
    """

    df[id_field] = df.groupby(list(args)).ngroup()

    return df

    This is a basic calculation, a more sophisticated method for calculating could be implemented."""