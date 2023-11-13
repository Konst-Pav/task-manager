from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('users/', include('task_manager.user.urls')),
    path('labels/', include('task_manager.label.urls')),
    path('statuses/', include('task_manager.status.urls')),
    path('tasks/', include('task_manager.task.urls')),
]
