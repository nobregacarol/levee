
# Data Engineer Code Challenge - Levee
Author: Caroline Nóbrega

## Installation
### Python project
Preparating the virtual environment to run the project. 

### Steps:
1. Go to the project directory and open a terminal. 
2. Run *python -m venv .venv* to create the virtual environment for this project.
3. Go to *.venv/Scripts* and activate the virtual environment executing the **activate.bat** file.
4. Setup the pip package manager.
5. Run *pip install -r requirements.txt* to install the dependencies. 
6. Run *pip list* to see all libraries installed. 

### MySQL database
Preparating the database.

### Steps:
1. Use the **create_mysql.sql** file to create the levee schema, category and jobs tables on MySQL database.
2. Run *python db_load_data.py* to load the data from .txt files into database tables.

## First solution: data from txt file
The first solution uses the txt files to calculate the results. It only uses Python to complete the challenge.

1. Run *python txt_get_results.py*
2. See the results on terminal.

## Second solution: data from MySQL Database
The second solution uses the data from database tables to calculate the results. It uses Python and SQL to complete the challenge.

1. Run *python db_get_results.py*
2. See the results on terminal.


