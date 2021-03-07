from src.celery import app
from time import sleep


@app.task
def hard_task(i=3):
    print(i)
    for j in range(i):
        sleep(1)
        print(j)

