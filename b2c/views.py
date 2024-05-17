from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import add
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


# Create your views here.

@csrf_exempt
def add_task(request):
    add.delay(4, 6)
    return JsonResponse({"message": "success"})


@csrf_exempt
def schedule_task(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS
    )
    PeriodicTask.objects.create(
        interval=interval,
        name='my_schedule',
        task='b2c.tasks.print_task',
        # args=json.dumps(['arg1', 'arg2'])
        # one_off=False
    )
    return JsonResponse({"message": "task scheduled successfully"})
