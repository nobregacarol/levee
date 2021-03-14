
# Data Engineer Code Challenge - Levee
Autor: Caroline Nóbrega

## Installation
### Python project
Preparating the virtual environment to run the project.

### Steps:
1. Go to the project directory and open a terminal. 
2. Run *python -m venv .venv*.
3. Go to *.venv/Scripts* and activate the virtual environment executing the **activate.bat** file.
4. Setup the pip package manager.
5. Run *pip install -r requirements.txt* to install the dependencies. 

### MySQL database
Preparating the database.

### Steps:
1. Use the **create_mysql.sql** file to create the levee schema, category and jobs tables on an MySQL database.
2. Run *python db_load_data.py* to load the data from txt files into database tables.

## First solution: data from txt file
The first solution uses the txt files to calculate the results. It only uses Python to resolve the challenge.

1. Run *python txt_get_results.py*

## Second solution: data from MySQL Database
The first solution uses the data from database tables to calculate the results. It uses Python and SQL to resolve the challenge.

1. Run *python db_get_results.py*


