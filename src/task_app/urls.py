from django.urls import path
from .views import *

urlpatterns = [
    path("task/", TaskView.as_view(), name="tasks")
]