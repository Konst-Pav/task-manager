from django.forms import ModelForm
from task_manager.task.models import Task
from django import forms
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _
from task_manager.user.forms import UserModelChoiceField


class TaskForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
    )
    description = forms.CharField(
        label=_('Description'),
        label_suffix='',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none', 'placeholder': _('Description')}),
    )
    executor = UserModelChoiceField(
        queryset=User.objects.all(),
        label=_('Executor'),
        label_suffix='',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Status'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Label'),
        label_suffix='',
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiply': 'multiply'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
