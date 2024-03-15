from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label=_('Surname'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=_('Confirm the password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if self.instance:
            if User.objects.exclude(id=self.instance.pk).filter(username__iexact=username).first():
                return super().clean_username()
            return username
        return super().clean_username()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')}),
            'first_name': forms.TextInput(attrs={'class': 'form-label', 'placeholder': _('Your name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-label', 'placeholder': _('Your last name')}),
            'password1': forms.PasswordInput(attrs={'class': 'form-label', 'placeholder': _('Password')}),
            'password2': forms.PasswordInput(attrs={'class': 'form-label', 'placeholder': _('Password confirmation')})
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'),
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')})
    )
    password = forms.CharField(
        label=_('Password'),
        # label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password'), 'label_suffix': ''})
    )
