from django.urls import path
from task_manager.task import views


urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks_index'),
    path('<int:task_id>/', views.TaskReadView.as_view(), name='tasks_read'),
    path('create/', views.TaskCreateView.as_view(), name='tasks_create'),
    path('<int:task_id>/edit/', views.TaskUpdateView.as_view(), name='tasks_update'),
    path('<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='tasks_delete'),
]
