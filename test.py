import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import sys
import datetime


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    cur.execute('select * from songs')
    x = cur.fetchall()
    print(list(x))


if __name__ == "__main__":
    main()
