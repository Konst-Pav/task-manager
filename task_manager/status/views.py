from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.permissions import LoginRequiredMixinWithMessage
from django.utils.translation import gettext as _
from task_manager.mixins import ProtectedErrorHandlerMixin


class StatusIndexView(LoginRequiredMixinWithMessage, ListView):
    model = Status
    template_name = 'status/index.html'
    context_object_name = 'statuses'


class StatusCreateView(
    LoginRequiredMixinWithMessage,
    SuccessMessageMixin,
    CreateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'status/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully created')
    login_url = reverse_lazy('login_view')


class StatusUpdateView(
    LoginRequiredMixinWithMessage,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully changed')
    login_url = '/login/'


class StatusDeleteView(
    LoginRequiredMixinWithMessage,
    ProtectedErrorHandlerMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully deleted')
    login_url = '/login/'
    error_message = _('It is not possible to delete the status because it is in use')  # noqa: E501
    redirect_url = reverse_lazy('statuses_index')
