import pandas as pd

def value_count_column(df, column_name):
    """Prints value_counts for a column in df.

    Args:
        df: The pandas DataFrame.
        column_name: The name of the numerical column.
    """
    print(df[column_name].value_counts(ascending=False))
    print('\n')


