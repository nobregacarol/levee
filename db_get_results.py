# Data Engineer Code Challenge - Levee

# Importing libraries
from mysql_adapter import Database
import pandas as pd
from datetime import date

# Instantiating database class
database = Database()

# Opening connection to MySQL local instance
conn, cursor = database.open("localhost", 3306, "levee_man", "levee_man")

try:
    # Solution 1 - The number of Open Positions per Category Name

    # Executing Query 1
    sql = """
        SELECT category.title, SUM(jobs.open_position_amount) as sum
        FROM levee.jobs as jobs
        LEFT JOIN levee.category as category ON category.category_id = jobs.category_id
        GROUP BY category.title
        ORDER BY category.title ASC
        """

    cursor.execute(sql)
    result = cursor.fetchall()

    # Printing results
    print("The number of Open Positions per Category Name: \n")
    for item in result:
        print(
            "Category: "
            + item["title"]
            + " - Open position amount: "
            + str(item["sum"])
        )

    print("\n")

    # Solution 2 - The last three Jobs that have expired

    # Getting current date
    date = date.today()

    # Executing Query 2
    sql = """
        SELECT category.title, jobs.*
        FROM levee.jobs as jobs
        LEFT JOIN levee.category as category ON category.category_id = jobs.category_id
        WHERE jobs.expires_at < %s
        ORDER BY jobs.expires_at DESC
        LIMIT 3
        """

    cursor.execute(sql, (date,))
    result = cursor.fetchall()

    # Printing results
    print("The last three Jobs that have expired: \n")
    for item in result:
        print(
            "Category: "
            + item["title"]
            + " - Job title: "
            + item["job_title"]
            + " - Expire date: "
            + item["expires_at"].strftime("%d/%m/%Y")
        )

    # Closing connection to MySQL local instance
    database.close(conn)

# Generating error message if something goes wrong
except Exception as error:
    print("Error", str(error))
