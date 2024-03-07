from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from task_manager.label.models import Label


class LabelForm(ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
    )

    class Meta:
        model = Label
        fields = ['name', ]
