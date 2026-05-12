import pandas as pd
import re

def clean_dataframe(input_file, output_file):
    """
    Cleans a CSV dataset by removing:
    1. Links from the 'Text' column.
    2. Posts without a title and with removed text ('removed', 'remove', 'rimosso').
    3. Completely empty posts (without title and without text).
    4. Posts containing only the title and no text.

    The result is saved in a new CSV file.
    """
    # Load the dataset
    df = pd.read_csv(input_file, encoding="utf-8")

    # Remove links from the 'Text' column
    url_pattern = r"http[s]?://\S+|www\.\S+"
    df["Text"] = df["Text"].apply(lambda x: re.sub(url_pattern, "", x).strip() if isinstance(x, str) else x)

    # Remove posts without a title and without valid text
    df = df[~(
        ((df["Title"].isna()) | (df["Title"].str.strip() == "")) & 
        ((df["Text"].isna()) | (df["Text"].str.strip() == "") | (df["Text"].str.lower().str.strip().isin(["rimosso", "remove"])))
    )]

    # Remove posts with only the title
    before_count = len(df)
    df = df[~((df["Text"].isna()) | (df["Text"].str.strip() == ""))]
    removed_count = before_count - len(df)

    # Save the cleaned file
    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"Cleaned file saved: {output_file}")
    print(f"Number of posts removed because they had only the title: {removed_count}")

# Usage example
clean_dataframe("input.csv", "output_clean.csv")
