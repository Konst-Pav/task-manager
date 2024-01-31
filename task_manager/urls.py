from django.contrib import admin
from django.urls import path, include
from task_manager import views
from task_manager.user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index_view'),
    path('login/', user_views.LoginUserView.as_view(), name='login_view'),
    path('logout/', user_views.logout_user, name='logout'),
    path('users/', include('task_manager.user.urls')),
    path('labels/', include('task_manager.label.urls')),
    path('statuses/', include('task_manager.status.urls')),
    path('tasks/', include('task_manager.task.urls')),
]
