from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import add

# Create your views here.


@csrf_exempt
def add_task(request):
    add.delay(4, 6)
    return JsonResponse({"message": "success"})
