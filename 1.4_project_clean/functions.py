import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple, Dict, Any, List


# Functions
def compute_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Computes missing values with percentages for each column in the dataframe."""
    missing_values = data.isnull().sum()
    missing_values_percentage = round((data.isnull().sum() / len(data)) * 100, 2)

    # Combine the counts and percentages into a dataframe for a clearer view
    missing_values_df = pd.DataFrame(
        {"Missing Values": missing_values, "Percentage (%)": missing_values_percentage}
    ).sort_values(by="Percentage (%)", ascending=False)

    # Filter to include only columns where missing value count > 0
    missing_values_df = missing_values_df[
        missing_values_df["Missing Values"] > 0
    ].sort_values(by="Percentage (%)", ascending=False)
    missing_values_df = missing_values_df.sort_values(
        by="Percentage (%)", ascending=False
    )

    return missing_values_df


def not_alphanumeric_columns(data: pd.DataFrame, pattern=r"[^a-zA-Z0-9\s]") -> list:
    """Give a list of columns with non-alphanumeric characters in a DataFrame."""

    columns_with_symbols = []

    for column in data.columns:
        if (
            data[
                data[column].astype(str).str.contains(pattern, na=False, regex=True)
            ].shape[0]
            > 0
        ):
            columns_with_symbols.append(column)

    return columns_with_symbols


def not_alphanumeric(
    data: pd.DataFrame, column: str, pattern=r"[^a-zA-Z0-9\s]"
) -> pd.Series:
    """View entries with non-alphanumeric characters for a specific column in a DataFrame."""

    return data[data[column].astype(str).str.contains(pattern, na=False, regex=True)][
        column
    ]


def outliers_numerical_cols(df: pd.DataFrame) -> None:
    """Visualize outliers in numerical columns using boxplots."""
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
    """Visualize distribution of numerical columns using histograms."""
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
    """Check if a column has outliers using IQR."""
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((column_data < lower_bound) | (column_data > upper_bound)).any()


def analyze_categorical_column(
    dataframe: pd.DataFrame, column_name: str
) -> Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame, List[str]]:
    """Analyze a categorical column of a given DataFrame.

    Args:
        dataframe (pd.DataFrame): Input dataframe containing the column to be analyzed.
        column_name (str): Name of the categorical column to analyze.

    Returns:
        Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame, List[str]]: A tuple containing
        analysis results as a dictionary,
        dataframes with the shortest and longest values,
        and a list of non-string columns.
    """
    analysis_results = {}
    non_str_columns = []

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


def column_max_lengths(dataframe: pd.DataFrame, categorical_columns: List[str]) -> None:
    """
    Display the maximum string lengths of specified columns in a given dataframe.

    Args:
        dataframe (pd.DataFrame): The dataframe containing the columns to be analyzed.
        columns (List[str]): List of column names whose maximum string lengths are to be displayed.

    Returns:
        None: The function prints the results and does not return any value.
    """

    print("Column Name".ljust(30), "Max Length".ljust(10))
    print("-" * 40)
    for column in categorical_columns:
        max_length = dataframe[column].str.len().max()
        print(f"{column.ljust(30)} {str(max_length).ljust(10)}")


def df_col_max_lengths(dataframe: pd.DataFrame) -> None:
    """
    Display the maximum string lengths of categorical columns in a given dataframe.
    """
    categorical_columns = dataframe.select_dtypes(
        include=["string", "object"]
    ).columns.tolist()

    print("Column Name".ljust(30), "Max Length".ljust(10))
    print("-" * 40)
    for column in categorical_columns:
        max_length = dataframe[column].str.len().max()
        print(f"{column.ljust(30)} {str(max_length).ljust(10)}")


def lowercase_column_names(df):
    """Convert all column names in a DataFrame to lowercase."""
    # Usage: df = lowercase_column_names(df)
    # Works same as: df.columns = [c.lower() for c in df.columns]
    df.columns = [col.lower() for col in df.columns]
    return df


def factorize_id(df: pd.DataFrame, *args, id_field: str) -> pd.DataFrame:
    """
    Create a serialized INT value for each unique combination of
    specified columns.

    Args:
        df (pd.DataFrame): Input dataframe.
        *args: Columns to be used for unique combinations.
        id_field (str): Name of the new ID field.

    Returns:
        pd.DataFrame: DataFrame with a new ID field.
    """

    combined = df[list(args)].astype(str).agg("_".join, axis=1)

    df[id_field] = pd.factorize(combined)[0] + 1

    return df
