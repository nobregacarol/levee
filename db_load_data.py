# Data Engineer Code Challenge - Levee

# Importing libraries
from mysql_adapter import Database
import pandas as pd

# Loading data from txt files into python dataframes
jobs_df = pd.read_csv("jobs.txt", delimiter="|")
category_df = pd.read_csv("category.txt", delimiter="|")

# Changing expire date from string to datetime
jobs_df["ExpiresAt"] = pd.to_datetime(jobs_df["ExpiresAt"])
# Replacing nan values to null values
jobs_df.replace("nan", "")

# Instantiating database class
database = Database()

# Opening connection to MySQL local instance
conn, cursor = database.open("localhost", 3306, "levee_man", "levee_man")

try:
    # Inserting data from category txt file into MySQL table
    sql = """
        INSERT INTO levee.category (category_id, title) VALUES (%s, %s);
        """
    val = [
        (dictinary["id"], dictinary["name"])
        for dictinary in category_df.to_dict("records")
    ]

    cursor.executemany(sql, val)
    conn.commit()
    print(cursor.rowcount, "was inserted.")

    # Inserting data from jobs txt file into MySQL table
    sql = """
        INSERT INTO levee.jobs (partner_id, job_title, category_id, expires_at, open_position_amount) VALUES (%s, %s, %s, %s, %s);
        """
    val = [
        (
            dictinary["partnerId"],
            dictinary["title"],
            dictinary["categoryId"],
            dictinary["ExpiresAt"],
            dictinary["openPositionAmnt"],
        )
        for dictinary in jobs_df.to_dict("records")
    ]

    cursor.executemany(sql, val)
    conn.commit()
    print(cursor.rowcount, "was inserted.")

    # Closing connection to MySQL local instance
    database.close(conn)

# Generating error message if something goes wrong
except Exception as error:
    print("Error", str(error))
