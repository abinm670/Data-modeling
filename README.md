# Data Modeling with Postgres:
Build a database from the Sparkify app. Define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL which would help the analysis team to run queries that leads to answer questions and find insights.


# Project Template

#### Project Steps

* Create Tables
Run create_tables.py to create your database and tables.
Run test.ipynb to confirm the creation of your tables with the correct columns. 
* Build ETL Processes
Run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

***  NOTE: You will not be able to run test.py, etl.py, or etl.py until you have run create_tables.py at least once to create the sparkifydb database, which these other files connect to.


# Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

#### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
#### Dimension Tables
users - users in the app
user_id, first_name, last_name, gender, level
songs - songs in music database
song_id, title, artist_id, year, duration
artists - artists in music database
artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday



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



