from django.forms import ModelForm
from task_manager.task.models import Task
from django import forms
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _
from task_manager.user.forms import UserModelChoiceField


class TaskForm(ModelForm):
    name = forms.CharField(label=_('Name'))
    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={'style': 'resize:none'}
        ),
    )
    executor = UserModelChoiceField(
        queryset=User.objects.all(),
        label=_('Executor'),
        required=False,
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Status'),
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Labels'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'multiply': 'multiply',
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
