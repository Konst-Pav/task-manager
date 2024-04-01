from django import forms
from django.forms import ModelForm
from task_manager.status.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(ModelForm):
    name = forms.CharField(label=_('Name'))

    class Meta:
        model = Status
        fields = ['name', ]
