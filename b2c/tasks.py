import time

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


@shared_task
def add(x, y):
    time.sleep(15)
    return x + y


@shared_task
def print_task():
    print("SCHEDULED TASK RUNNING")
    return

