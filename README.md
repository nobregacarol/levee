
# Data Engineer Code Challenge - Levee
Author: Caroline Nóbrega

## Installation
### Python project

### Steps to prepare environment:
1. Go to the project directory and open a terminal. 
2. Run *python -m venv .venv* to create the virtual environment for this project.
3. Go to *.venv/Scripts* and activate the virtual environment executing the **activate.bat** file.
4. Setup the pip package manager.
5. Run *pip install -r requirements.txt* to install the dependencies. 
6. Run *pip list* to see all libraries installed. 

### MySQL database

### Steps to load data into database:
1. Use the **create_mysql.sql** file to create the schema and tables.
2. Run *python db_load_data.py* to load the data from .txt files into database tables.

## First solution: data from .txt file
The first solution uses the txt files to calculate the results. It only uses Python to complete the challenge.

1. Run *python txt_get_results.py*
2. See the result on terminal.

### Output 
For this solution the output has a dataframe format.

- **Output for the current .txt file data:**

| name           |  ---   
| ---            | :--:   
| Administrativo | 17     
| Atendimento    | 36      
| Tecnologia     | 6     
| Vendas         | 18     

| partnerId | title              | categoryId | ExpiresAt  | openPositionAmnt | name
| ---       | ---                | ---        | ---        | ---              | :--:
| 909       | Vendedor Externo   | 3          | 2020-12-16 | 1                | Vendas
| 6899      | Promotor de Vendas | 3          | 2020-12-21 | 1                | Vendas
| 4435      | Office Boy         | 2          | 2020-12-25 | 1                | Administrativo

## Second solution: data from MySQL Database
The second solution uses the data from database tables to calculate the results. It uses Python and SQL to complete the challenge.

1. Run *python db_get_results.py*
2. See the result on terminal.

### Output 
For this solution the output has a text format.

- **Output for the current data:**

The number of Open Positions per Category Name: 

Category: Administrativo - Open position amount: 17

Category: Atendimento - Open position amount: 36

Category: Tecnologia - Open position amount: 6

Category: Vendas - Open position amount: 18


The last three Jobs that have expired:

Category: Administrativo - Job title: Office Boy - Expire date: 25/12/2020

Category: Vendas - Job title: Promotor de Vendas - Expire date: 21/12/2020

Category: Vendas - Job title: Vendedor Externo - Expire date: 16/12/2020

