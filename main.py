import pandas as pd
from fscore import f_score

if __name__ == "__main__":
    # Create a data-frame containing the fundamental data of firms
    data = pd.read_csv("./data/fundamentals.csv", index_col=0)

    # Specify the considered year to find the F-Score
    year = 2022

    # Calculate the F-Score and put into the data frame
    data["F-Score"] = f_score(data, year)

    # Print the "F-Score" column to the console
    print(data.to_string(columns=["F-Score"]))
