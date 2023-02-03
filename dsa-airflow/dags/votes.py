import os
from datetime import datetime
from collections import Counter
import pandas as pd
from airflow import DAG
from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from airflow.hooks.filesystem import FSHook

# global variable for flavor choices
flavors_choices = [
    "lemon",
    "vanilla",
    "chocolate",
    "pistachio",
    "strawberry",
    "confetti",
    "caramel",
    "pumpkin",
    "rose",
]
# global variable for votes file
FILE_NAME = "votes.csv"


@task
def read_file():
    """
    read votes file from a CSV

    This function uses an Airflow FileSystem Connection called "data_fs" as the root folder
    to look for the airports file. Make sure this FileSystem connection exists
    """
    # get the data_fs filesystem root path
    data_fs = FSHook(conn_id="data_fs")  # get airflow connection for data_fs
    data_dir = data_fs.get_path()  # get its root path
    print(f"data_fs root path: {data_dir}")

    # create the full path to the votes file
    file_path = os.path.join(data_dir, FILE_NAME)
    print(f"reading file: {file_path}")

    # read csv
    df = pd.read_csv(file_path, header=0)
    votes = df.votes.values.tolist()

    # loop over list to verify votes are on flavors_list
    valid_votes = []
    for i in votes:
        if i in flavors_choices:
            valid_votes.append(i)
    return valid_votes

@task
def add_votes(votes_list: list):
    """
    using counter to check with flavor had max votes
    """

    data = Counter(votes_list)
    max_vote = data.most_common(1)[0][0]

    print(f"The winning flavor is: {max_vote}!")


@dag(
    schedule_interval="@once",
    start_date=datetime.utcnow(),
    catchup=False,
    default_view="graph",
    is_paused_upon_creation=True,
)
def cake_final_vote():
    """get final vote"""

    # define the file sensor...
    # wait for the airports file in the "data_fs" filesystem connection
    wait_for_file = FileSensor(
        task_id='wait_for_file',
        poke_interval=55,
        timeout=(30 * 60),
        mode="poke",  # mode: poke, reschedule
        filepath=FILE_NAME,  # file path to check (relative to fs_conn)
        fs_conn_id='data_fs',  # file system connection (root path)
    )

    # read file
    read_file_task = read_file()

    # add votes
    add_votes_task = add_votes(read_file_task)

    # complete tasks
    wait_for_file >> read_file_task >> add_votes_task


# generate dag
dag = cake_final_vote()
