# By: Dexne
# Airflow

# Librerias necesarias
import logging  # monitorear la ejecucion de nuestro dag
from datetime import timedelta

from airflow import DAG
# importar los operadores de python ya que usaremos funciones de python
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# definicion de diccionario con parametros por default
default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'email':['airflow@example.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=5),
}

# tareas
def scrape():
    logging.info("performing scraping")

def process():
    logging.info("performing processing")

def save():
    logging.info("performing saving")

# Definir nuestro grafo aciclico dirigido
with DAG(
    'first',
    default_args= default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    
    # definicion de las tareas
    scrape_task = PythonOperator(task_id="scrape", python_callable=scrape)
    process_task = PythonOperator(task_id="process", python_callable=process)
    save_task = PythonOperator(task_id="save", python_callable=save)

    # Definir las dependencias entre nuestras tareas, orden
    scrape_task >> process_task >> save_task