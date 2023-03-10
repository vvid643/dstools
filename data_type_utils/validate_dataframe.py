from typing import Union, List

import pandas as pd
import pandas.api.types as ptypes


def has_column(data: pd.DataFrame, column: Union[List[str], str]) -> bool:
    if isinstance(column, list):
        return all([col in data.columns for col in column])
    elif isinstance(column, str):
        return column in data.columns
    else:
        raise TypeError("column arg should be either string or list of string")


def has_valid_dtype(data: pd.DataFrame, dtype_to_check: str) -> bool:
    if dtype_to_check == "str":
        return ptypes.is_string_dtype(data)
    elif dtype_to_check == "numeric":
        return all([ptypes.is_numeric_dtype(data[col]) for col in data.columns])
    else:
        raise ValueError(f"Type checking for {dtype_to_check} not configured")
