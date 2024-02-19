from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utils import LoginRequiredMixinWithMessage
from django.utils.translation import gettext as _


class StatusIndexView(LoginRequiredMixinWithMessage, ListView):
    model = Status
    template_name = 'status/index.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully created')
    login_url = reverse_lazy('login_view')


class StatusUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully changed')
    login_url = '/login/'


class StatusDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('The status has been successfully deleted')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – delete a status')
        body_title = _('Delete a status')
        body_subtitle = f"{_('Are you sure you want to delete the status')}: {context.get('status').name}"
        button_value = _('Yes, delete')
        context['body'] = {'title': body_title, 'subtitle': body_subtitle, 'button_value': button_value}
        return context
