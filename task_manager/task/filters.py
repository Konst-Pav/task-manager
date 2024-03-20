import django_filters
from django_filters import filters
from django.contrib.auth.models import User
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.label.models import Label
from task_manager.user.forms import UserModelChoiceField
from django import forms
from django.utils.translation import gettext_lazy as _


class UserModelChoiceFilter(django_filters.ModelChoiceFilter):
    field_class = UserModelChoiceField


class TaskFilter(django_filters.FilterSet):
    status = filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    executor = UserModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    self_tasks = django_filters.BooleanFilter(
        field_name='author',
        label=_('Only your own tasks'),
        label_suffix='',
        method='filter_self_tasks',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            user_id = self.request.user.id
            return queryset.filter(author_id=user_id)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_tasks']
