from django.urls import path
from task_manager.status import views


urlpatterns = [
    path('', views.StatusIndexView.as_view(), name='statuses_index'),
    path('<int:status_id>/create/', views.StatusCreateView.as_view(), name='statuses_create'),
    path('<int:status_id>/edit/', views.StatusUpdateView.as_view(), name='statuses_update'),
    path('<int:status_id>/delete/', views.StatusDeleteView.as_view(), name='statuses_delete'),
]
