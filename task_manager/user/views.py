from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from task_manager.user.forms import RegisterUserForm
from task_manager.user.forms import LoginUserForm
from task_manager.permissions import (
    EditingProfilePermissionMixin,
    LoginRequiredMixinWithMessage,
)
from task_manager.mixins import ProtectedErrorHandlerMixin


class UserIndexView(ListView):
    model = User
    template_name = "user/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = "user/create.html"
    success_url = reverse_lazy("login_view")
    success_message = _("The user has been successfully registered")


class UserUpdateView(
    LoginRequiredMixinWithMessage,
    SuccessMessageMixin,
    EditingProfilePermissionMixin,
    UpdateView,
):
    model = User
    form_class = RegisterUserForm
    template_name = "user/update.html"
    success_url = reverse_lazy("users_index")
    success_message = _("The user has been successfully changed")


class UserDeleteView(
    LoginRequiredMixinWithMessage,
    SuccessMessageMixin,
    ProtectedErrorHandlerMixin,
    EditingProfilePermissionMixin,
    DeleteView,
):
    model = User
    template_name = "user/delete.html"
    success_url = reverse_lazy("users_index")
    error_url = reverse_lazy("index_view")
    success_message = _("The user was successfully deleted")
    error_message = _("It is not possible to delete a user because it is being used")  # noqa: E501
    redirect_url = reverse_lazy("users_index")


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = "login.html"
    next_page = reverse_lazy("index_view")
    success_message = _("You are logged in")


def logout_user(request):
    logout(request)
    messages.info(request, _("You are logged out"))
    return redirect("index_view")
