import django_filters
from django.db import models
from django_filters import filters
from django.contrib.auth.models import User
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.label.models import Label
from django import forms


class TaskFilter(django_filters.FilterSet):
    status = filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    executor = filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    user_tasks = django_filters.BooleanFilter(
        field_name='author',
        label='',
        help_text='Только свои задачи',
        method='filter_user_tasks',
        widget=forms.CheckboxInput(),
    )

    def filter_user_tasks(self, queryset, name, value):
        if value:
            user_id = self.request.user.id
            return queryset.filter(author_id=user_id)
        return queryset

    class Meta:
        model = Task
        fields = ['executor', 'status', 'labels', 'user_tasks']
