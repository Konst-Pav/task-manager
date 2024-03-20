from django.urls import path
from task_manager.task import views


urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks_index'),
    path('<int:pk>/', views.TaskReadView.as_view(), name='tasks_read'),
    path('create/', views.TaskCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='tasks_delete'),
]
