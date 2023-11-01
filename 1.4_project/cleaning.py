"""
Utilities for data handling and manipulation.

This module provides tools using the pandas and numpy libraries for various 
data processing tasks.
"""

from typing import Union, List
import numpy as np
import pandas as pd


class DataCleaning:  # DataframeCleaner
    """
    A class designed to perform various data cleaning operations on a pandas DataFrame.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Constructor for the DataCleaning class.
        """
        self.data = data.copy()
        self.series = None
        self.default_value = 0

    def replace_to_none(self, value: Union[str, List[str], None] = None):
        """
        Replace specified values (or NaN by default) in the DataFrame with None.
        """
        if value is None:
            value = np.nan

        if not isinstance(
            value, list
        ):  # If a single string is provided, convert it to a list.
            value = [value]

        for replace in value:
            self.data.replace({replace: None}, inplace=True)
        return self.data

    def remove_duplicates(self):
        """
        Remove duplicate rows from the DataFrame.
        """
        self.data.drop_duplicates(keep="first", inplace=True)
        return self.data

    def remove_price_duplicates(self):
        """
        Remove duplicate value if any found. Keep rows with the lowest price.
        """
        if "price" not in self.data.columns:
            raise ValueError("The DataFrame does not have a 'price' column.")

        # Define columns to be considered for identifying duplicates.
        column_subset = self.data.columns.difference(["price"])

        # Sort DataFrame based on the 'price' column in ascending order.
        self.data.sort_values(by="price", inplace=True)

        # Drop duplicates, retaining the first occurrence (which will have the lowest price due to sorting).
        self.data.drop_duplicates(subset=column_subset, keep="first", inplace=True)
        return self.data

    def remove_brackets(self, column_name: str):
        """
        Removes [ and ] from a specified column in a DataFrame.
        """
        modified_column = self.data[column_name].str.replace("[\[\]]", "", regex=True)
        return modified_column

    def remove_single_quotes(self, column_name: List[str]):
        """
        Removes single quotes ' from a specified column in a DataFrame.
        """
        modified_column = self.data[column_name].str.replace("'", "")
        return modified_column

    # Number cleaning
    def number_cleaning(self, column_name: str, dtype="float"):
        """
        Utility to clean and convert columns in a DataFrame into numeric types.

        Methods:
        - number_cleaning: Converts a column into either float or int type.
        - _extract_float: Helper to extract/convert values to float.
        - _extract_int: Helper to extract/convert values to int.
        """
        if column_name not in self.data:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

        self.series = self.data[column_name]

        if dtype == "float":
            self.data[column_name] = self.series.apply(self._extract_float)
        elif dtype == "int":
            self.data[column_name] = self.series.apply(self._extract_int)
        else:
            raise ValueError(f"Unsupported dtype {dtype}")
        return self.data[column_name]

    def _extract_float(self, value):
        """Attempt to extract or convert a value into a float."""
        if pd.isna(value):  # Check if value is NaN
            return self.default_value
        try:
            return float(value)
        except ValueError:
            # If direct conversion fails, first remove all but the last period
            modified_value = value[::-1].replace(".", "", value.count(".") - 1)[::-1]
            # If direct conversion fails, extract the number from the string
            float_val = "".join(
                filter(lambda x: x.isdigit() or x == ".", modified_value)
            )
            if float_val:
                return float(float_val)
            else:
                index_value = self.series[self.series == value].index[0]
                print(
                    f"Failed to convert value '{value}' at index {index_value} to float."
                )
                return self.default_value

    def _extract_int(self, value):
        """Attempt to extract or convert a value into an integer."""
        if pd.isna(value):  # Check if value is NaN
            return self.default_value
        try:
            return int(value)
        except ValueError:
            # If direct conversion fails, extract the number from the string
            int_val = "".join(filter(lambda x: x.isdigit(), str(value)))
            if int_val:
                return int(int_val)
            else:
                index_value = self.series[self.series == value].index[0]
                print(
                    f"Failed to convert value '{value}' at index {index_value} to int."
                )
                return self.default_value
