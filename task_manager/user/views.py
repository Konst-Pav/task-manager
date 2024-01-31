from django.shortcuts import render
from django.views import View
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
from django.core.exceptions import ImproperlyConfigured

from task_manager.user.forms import RegisterUserForm
from task_manager.user.forms import LoginUserForm


class UserIndexView(ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('login_view')
    success_message = 'Пользователь успешно зарегистрирован'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно изменен'


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('index_view')
    error_url = reverse_lazy('index_view')
    success_message = 'Пользователь успешно удален'

    def post(self, request, *args, **kwargs):
        try:
            super().post(self, request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(request, messages.ERROR, 'Невозможно удалить пользователя, потому что он используется')
            return redirect(reverse_lazy('index_view'))


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    next_page = reverse_lazy('users_index')
    success_message = 'Вы залогинены'


def logout_user(request):
    logout(request)
    messages.success(request, "Вы разлогинены")
    return redirect('index_view')
