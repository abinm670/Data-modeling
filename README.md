# Data Modeling with Postgres:
Build a database from the Sparkify app. The main goal of this databse is to create a star schema that would help the analysis team to run queries that leads to answer your question and find insights.

### Project Repository files:
Create_tables.py file will create a sparkifydb database and import the sql_queries.py to create the fact table and four dimension tables. Finally, the test file will check for if the data exist in the songs table.


### Build ETL Pipeline:
First will create tables by runing create_tables.py file, and once the tables ready, run the etl.py file, this file will extartc the json files from the working directory, transform datatype and finaly load the data into the star schema.


### Run the Project:
* python create_tables.py
* python etl.py

### Test the project:
test.py 





# Refrence:

#### Change data type of a specific column of a pandas dataframe
https://stackoverflow.com/questions/41590884/#### change-data-type-of-a-specific-column-of-a-pandas-dataframe

#### solve the OutOfBoundsDatetime:
https://github.com/pandas-dev/pandas/issues/10987

#### Python datetime fromtimestamp yielding valueerror year out of range [duplicate]
https://stackoverflow.com/questions/10286224/javascript-timestamp-to-python-datetime-conversion
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

#### Datetime converting:
https://www.geeksforgeeks.org/python-pandas-to_datetime/



