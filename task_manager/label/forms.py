from django.forms import ModelForm
from django import forms
from task_manager.label.models import Label


class LabelForm(ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
    )

    class Meta:
        model = Label
        fields = ['name', ]
