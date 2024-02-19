from django.forms import ModelForm
from django import forms
from task_manager.label.models import Label
from django.utils.translation import gettext as _


class LabelForm(ModelForm):
    name = forms.CharField(
        label=_('Label name'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
    )

    class Meta:
        model = Label
        fields = ['name', ]
