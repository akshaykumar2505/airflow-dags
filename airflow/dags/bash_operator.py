from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="example_bash_operator",
    schedule="*/5 * * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "bash"],
    params={"example_key": "example_value"},
) as dag:
    
    # [START]
    run_this = BashOperator(
        task_id="task_id",
        bash_command="echo 'my bash command'",
    )
    # [END]
