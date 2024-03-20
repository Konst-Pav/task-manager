from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.permissions import LoginRequiredMixinWithMessage
from django.utils.translation import gettext as _
from task_manager.utils import ProtectedErrorHandlerMixin


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
    template_name = 'create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully created')
    login_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – create a status')
        body = {'title': _('Create a status'), 'button_value': _('create')}
        context['body'] = body
        return context


class StatusUpdateView(
    LoginRequiredMixinWithMessage,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully changed')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – change the status')
        body = {'title': _('Change the status'), 'button_value': _('edit')}
        context['body'] = body
        return context


class StatusDeleteView(
    LoginRequiredMixinWithMessage,
    ProtectedErrorHandlerMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully deleted')
    login_url = '/login/'
    error_message = _('It is not possible to delete the status because it is in use')  # noqa: E501
    redirect_url = reverse_lazy('statuses_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – delete a status')
        body_title = _('Delete a status')
        body_subtitle = f"{_('Are you sure you want to delete the status')}: {context.get('status').name}"  # noqa: E501
        button_value = _('Yes, delete')
        context['body'] = {
            'title': body_title,
            'subtitle': body_subtitle,
            'button_value': button_value,
        }
        return context
