from django.urls import path

from b2c import views

urlpatterns = [
    path("", views.add_task),
    path("schedule/", views.schedule_task)
]
