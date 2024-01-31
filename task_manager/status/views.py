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


class StatusIndexView(LoginRequiredMixinWithMessage, ListView):
    model = Status
    template_name = 'status/index.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно создан'
    login_url = reverse_lazy('login_view')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class StatusUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно изменен'
    login_url = '/login/'


class StatusDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно удален'
    login_url = '/login/'
