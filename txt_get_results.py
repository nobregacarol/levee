# Data Engineer Code Challenge - Levee

# Importing libraries
import pandas as pd
from datetime import datetime

# Loading data from txt files into python dataframes
jobs_df = pd.read_csv("jobs.txt", delimiter="|")
category_df = pd.read_csv("category.txt", delimiter="|")

# Joining python dataframes into one
joined_df = jobs_df.join(category_df.set_index("id"), on="categoryId")

# Solution 1 - The number of Open Positions per Category Name
sum_joined_df = joined_df.groupby(["name"]).sum()
open_positions_df = sum_joined_df["openPositionAmnt"]
print("The number of Open Positions per Category Name: \n")
print(open_positions_df)
print("\n")

# Solution 2 - The last three Jobs that have expired
date = datetime.today()

joined_df["ExpiresAt"] = pd.to_datetime(joined_df["ExpiresAt"])
expired_positions_df = (
    joined_df.loc[joined_df["ExpiresAt"] < date].sort_values("ExpiresAt").iloc[-3:]
)
print("The last three Jobs that have expired: \n")
print(expired_positions_df)
