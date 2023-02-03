import os
from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from airflow.hooks.filesystem import FSHook

# global variable for votes file
VOTES_FILE_NAME = 'votes.csv'
# global variable for flavor choices
flavors_choices = ["lemon", "vanilla", "chocolate", "pistachio", "strawberry", "confetti", "caramel", "pumpkin", "rose"]

@task
def read_file():
    """
    read votes file from a CSV

    This function uses an Airflow FileSystem Connection called "data_fs" as the root folder
    to look for the airports file. Make sure this FileSystem connection exists
    """
    # get the data_fs filesystem root path
    data_fs = FSHook(conn_id='data_fs')     # get airflow connection for data_fs
    data_dir = data_fs.get_path()           # get its root path
    print(f"data_fs root path: {data_dir}")

    # create the full path to the votes file
    file_path = os.path.join(data_dir, VOTES_FILE_NAME)
    print(f"reading file: {file_path}")

    # read csv
    df = pd.read_csv(file_path, header=0)

