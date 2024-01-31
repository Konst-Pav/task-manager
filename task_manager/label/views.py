from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from task_manager.utils import LoginRequiredMixinWithMessage
from task_manager.label.models import Label
from task_manager.label.forms import LabelForm


class LabelIndexView(LoginRequiredMixinWithMessage, ListView):
    model = Label
    template_name = 'label/index.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label/create.html'
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно создана'


class LabelUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'label/update.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно изменена'
    login_url = reverse_lazy('login_view')


class LabelDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно удалена'
    login_url = reverse_lazy('login_view')
