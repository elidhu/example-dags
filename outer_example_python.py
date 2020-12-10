from datetime import datetime

from airflow import DAG

from airflow.operators.python_operator import PythonOperator

default_args = {'owner': 'airflow',
                'start_date': datetime(2020, 11, 21)
               }

dag = DAG('outer_hello_world',
          schedule_interval='@daily',
          default_args=default_args,
          catchup=False)


def hello_world_py():
    print('Hello World... from the outside.')


with dag:
    t1 = PythonOperator(
        task_id='outer_hello_world',
        python_callable=hello_world_py)
