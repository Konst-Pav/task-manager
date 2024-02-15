from django.forms import ModelForm
from task_manager.task.models import Task
from django import forms
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label


class TaskForm(ModelForm):
    executors = User.objects.all()

    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
    )
    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none', 'placeholder': 'Описание'}),
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Исполнитель',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label='Метки',
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiply': 'multiply'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'executor', 'status', 'labels']

#
# class TaskFilterForm(forms.Form):
#
#     status = forms.ModelChoiceField(
#         queryset=Status.objects.all(),
#         label='Статус',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-select'}),
#     )
#     executor = forms.ModelChoiceField(
#         queryset=User.objects.all(),
#         label='Исполнитель',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-select'}),
#     )
#     label = forms.ModelChoiceField(
#         queryset=Label.objects.all(),
#         label='Метка',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-select'}),
#     )
#     user_tasks = forms.BooleanField(
#         label='',
#         help_text='Только свои задачи',
#         required=False,
#         widget=forms.Select(attrs={'class': 'form-check-label'}),
#     )
