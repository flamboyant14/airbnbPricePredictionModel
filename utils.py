import pandas as pd

class utilities:
    def check_value_counts(df: pd.DataFrame, columns: list):
        for col in columns:
            print(f"Value counts for {col}:\n{df[col].value_counts(dropna=False)}\n")