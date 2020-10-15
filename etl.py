import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import sys
import datetime

'''Transform Load function'''
def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id',
                    'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = df[['artist_id', 'artist_name',
                      'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)

''' Transform Load functions '''
def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')

    # insert time data records
    time_data = {'start_time': t, 'hour': t.dt.hour, 'day': t.dt.day,
                 'week': t.dt.isocalendar().week, 'month': t.dt.month, 'year': t.dt.year,
                 'weekday': t.dt.dayofweek}
    time_df = pd.DataFrame.from_dict(time_data)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        result = cur.fetchone()

        if result:
            songid, artistid = result
        else:
            continue

        ts_new = pd.to_datetime(row.ts, unit='ms')

        # insert songplay record
        songplay_data = (ts_new, row.userId, row.level, songid, artistid,
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

''' This function will collect JSON files and save it to a variable.
loop inside the variable and pass each file to the Transform Load functions.   '''
def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):

        ''' collect json files '''
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            # get the absolut path of file.json
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    # print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{} files processed out of : {}/{}'.format(i, num_files, datafile))

'''
The main function:
- connect to the database, create a cursor object to interact with the database.
- call process_data method to process and collect data from two different paths.
- calling a function inside a function. 
'''
def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
