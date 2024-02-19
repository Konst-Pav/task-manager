from django.forms import ModelForm
from task_manager.task.models import Task
from django import forms
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext as _


class TaskForm(ModelForm):
    executors = User.objects.all()

    name = forms.CharField(
        label=_('Task name'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none', 'placeholder': _('Description')}),
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_('Executor'),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Status'),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Label'),
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiply': 'multiply'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'executor', 'status', 'labels']
