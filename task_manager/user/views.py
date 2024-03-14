from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.utils.translation import gettext_lazy as _

from task_manager.user.forms import RegisterUserForm
from task_manager.user.forms import LoginUserForm
from task_manager.permissions import EditingProfilePermissionMixin, LoginRequiredMixinWithMessage
from task_manager.utils import ProtectedErrorHandlerMixin


class UserIndexView(ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'create.html'
    success_url = reverse_lazy('login_view')
    success_message = _('The user has been successfully registered')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – create a user')
        body = {'title': _('Registration'), 'button_value': _('register')}
        context['body'] = body
        return context


class UserUpdateView(LoginRequiredMixinWithMessage, EditingProfilePermissionMixin, UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'update.html'
    success_url = reverse_lazy('users_index')
    success_message = _('The user has been successfully changed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – update the user profile')
        body = {'title': _('Change the user'), 'button_value': _('edit')}
        context['body'] = body
        return context


class UserDeleteView(LoginRequiredMixinWithMessage, ProtectedErrorHandlerMixin, EditingProfilePermissionMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('index_view')
    error_url = reverse_lazy('index_view')
    success_message = _('The user was successfully deleted')
    error_message = _('It is not possible to delete a user because it is being used')
    redirect_url = reverse_lazy('users_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – delete a user')
        user_full_name = f"{context.get('user').first_name} {context.get('user').last_name}"
        body_title = _('Delete a user')
        body_subtitle = f"{_('Are you sure you want to delete the user')}: {user_full_name}"
        button_value = _('Yes, delete')
        context['body'] = {'title': body_title, 'subtitle': body_subtitle, 'button_value': button_value}
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    next_page = reverse_lazy('users_index')
    success_message = _('You are logged in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – login')
        return context


def logout_user(request):
    logout(request)
    messages.success(request, _('You are logged out'))
    return redirect('index_view')
