# tasks/urls.py
from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView,TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('api/tasks/', TaskListView.as_view(), name='task-list'), # List all tasks
    path('create/', TaskCreateView.as_view(), name='task-create'),    # Create a new task
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),#http://127.0.0.1:8000/api/tasks/1/ (replace 1 with the actual task ID)
    path('api/update/tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),#http://127.0.0.1:8000/api/tasks/1/update/ (replace 1 with the actual task ID)
    path('api/delete/tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),# http://127.0.0.1:8000/api/tasks/1/delete/ (replace 1 with the actual task ID)
    # path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
