import datetime
import sys
import os

from airflow import DAG

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()



