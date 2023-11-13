from django.urls import path
from task_manager.label import views


urlpatterns = [
    path('', views.LabelIndexView.as_view(), name='labels_index'),
    path('create/', views.LabelCreateView.as_view(), name='labels_create'),
    path('<int:label_id>/edit/', views.LabelUpdateView.as_view(), name='labels_update'),
    path('<int:label_id>/delete/', views.LabelDeleteView.as_view(), name='labels_delete'),
]
