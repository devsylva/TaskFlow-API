from django.urls import path
from .views import *

urlpatterns = [
    path("task_view/", TaskView.as_view()),
    path("task_detail/<str:pk>/", TaskDetail.as_view()),
    path("tag_view/", TagView.as_view()),
    path("tag_detail/<str:pk>/", TaskDetail.as_view()),
]