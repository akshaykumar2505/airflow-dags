from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="example_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:

    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )

    # [START]
    run_this = BashOperator(
        task_id="task_id",
        bash_command="echo 'my bash command'",
    )
    # [END]

    run_this >> run_this_last

    

if __name__ == "__main__":
    dag.test()