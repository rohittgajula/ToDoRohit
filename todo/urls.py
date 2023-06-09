from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name="task"),  # it automatically imports task_list.html file
    path('task-create/',TaskCreate.as_view(), name="task-create" ),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
]

