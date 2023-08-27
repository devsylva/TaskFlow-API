from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsTaskOwner
from django.http import Http404



# Create your views here.
class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    """
    list all task or create a new task
    """
    def get(self, request, format=None):
        if "category" in request.GET:
            category = request.GET["category"]
            categoryid = get_object_or_404(Category, name=category).id
            tasks = get_list_or_404(Task, user=request.user, category=categoryid)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        elif "tag" in request.GET:
            tag = request.GET["tag"]
            tagid = get_object_or_404(Tag, user=request.user, name=tag).id
            tasks = get_list_or_404(Task, user=request.user, tag=tagid)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        elif "status" in request.GET:
            status = request.GET["status"]
            tasks = get_list_or_404(Task, user=request.user, status=status)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        elif "priority" in request.GET:
            priority = request.GET["priority"]
            tasks = get_list_or_404(Task, user=request.user, priority=int(priority))
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

        tasks = Task.objects.filter(user=request.user).order_by('priority', 'deadline')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response({
            "success": True,
            "message": "Task deleted"
        },status=status.HTTP_204_NO_CONTENT)


class TagView(APIView):
    permission_classes = [IsAuthenticated]
    """
    list all task or create a new task
    """
    def get(self, request, format=None):
        tags = Tag.objects.filter(user=request.user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    """
    list all task or create a new task
    """
    def get(self, request, format=None):
        tags = Tag.objects.filter(user=request.user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)