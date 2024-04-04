import pandas as pd


def _column_to_list(df, column_name):
    """
    Converts a specified column in a pandas DataFrame to a list.

    Parameters:
    - df: The pandas DataFrame containing the column.
    - column_name: The name of the column to convert to a list.

    Returns:
    - A list containing the values of the specified column.
    """
    if column_name in df.columns:
        return df[column_name].tolist()
    else:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")


def _read_csv(csv_name):
    return pd.read_csv(csv_name)


def _drop_na(df, column):
    return df.dropna(subset=[column])
