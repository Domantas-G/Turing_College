import pandas as pd


class DataframeCleaner:
    """Class for data cleaning and manipulation, primarily for working on a pandas dataframe."""

    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.series = None
        self.default_value = 0

    def remove_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        self.data.drop_duplicates(keep="first", inplace=True)
        return self.data

    def remove_column_duplicates(self, column_name: str):
        """Remove duplicate value if any found. Keep rows with the lowest price."""
        if column_name not in self.data.columns:
            raise ValueError(f"The DataFrame does not have a '{column_name}' column.")

        column_subset = self.data.columns.difference([column_name])

        # Sort DataFrame based on the column in ascending order.
        self.data.sort_values(by=column_name, inplace=True)

        # Drop duplicates retaining the first occurrence.
        self.data.drop_duplicates(subset=column_subset, keep="first", inplace=True)
        return self.data

    def remove_brackets_and_quotes(self, column_name: str):
        """
        Removes [ ], and ' from a specified column in a DataFrame.
        """
        self.data[column_name] = self.data[column_name].str.replace(
            "[\[\]'']", "", regex=True
        )
        return self.data[column_name]  # Return only the processed column

    def missing_to_zero(self, column_name: str):
        """
        Replace missing values in the specified column with 0 if it's a numeric column,
        or "None" if it's a String/Object column.
        """
        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

        if pd.api.types.is_numeric_dtype(self.data[column_name]):
            self.data[column_name].fillna(0, inplace=True)
        else:
            self.data[column_name].fillna("None", inplace=True)
            self.data[column_name].replace("", "None", inplace=True)
        return self.data[column_name]

    def missing_to_median_or_mode(self, column_name: str):
        """
        Replace missing values in the specified column with median if it's a numeric column,
        or mode if it's a String/Object column.
        """
        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

        if pd.api.types.is_numeric_dtype(self.data[column_name]):
            self.data[column_name].fillna(self.data[column_name].median(), inplace=True)
        else:
            mode_value = self.data[column_name].mode().iloc[0]
            self.data[column_name].fillna(mode_value, inplace=True)
        return self.data[column_name]  # Return only the processed column

    def generate_factor_id(self, id_columns: list, id_field: str):
        """
        Generate primary keys from specified columns in the DataFrame.

        Parameters:
            id_columns (list): List of column names from which primary keys are generated.
            id_field (str): The name of the new primary key column.

        Returns:
            pd.DataFrame: The DataFrame with primary key columns added.

        Description:
            The method generates primary keys for the DataFrame based on the specified 'id_columns'.
            It uses the 'pd.factorize()' function to convert categorical data into numerical codes.
            The method creates unique integer identifiers for each combination of values in the selected 'id_columns'.
            The primary key values start from 1 and increment by 1 for each unique combination of values.
            The new primary key column is added to the DataFrame with the name specified by 'id_field'.
        """
        self.data.sort_index(inplace=True)

        self.data[id_field] = (
            pd.factorize(self.data[id_columns].apply(tuple, axis=1))[0] + 1
        )
        return self.data

    def add_id(df):
        """Add an 'id' column to the DataFrame based on the index."""
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input should be a pandas DataFrame.")

        df = df.reset_index(drop=True)
        df["id"] = df.index + 1

        return df
