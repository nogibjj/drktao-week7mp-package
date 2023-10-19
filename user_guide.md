## User instructions on how to install and use the command line tool

To access the etl-package command line tool, run setup.py in the terminal using `python setup.py develop`. This will allow us to subsequently use etl-package as a command to run this project as an executable. 

etl-package requires one argument to run our ETL and CRUD operations. This is simply the name of the database that is generated from transform_load.py. In this case, we should use `etl-package 'GroceryDB.db'` in the terminal. This simple command will run all extraction, loading, and CRUD functions contained within this project.
