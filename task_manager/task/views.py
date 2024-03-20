from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.permissions import LoginRequiredMixinWithMessage
from task_manager.task.filters import TaskFilter
from django_filters.views import FilterView
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib import messages


class TaskIndexView(LoginRequiredMixinWithMessage, FilterView):
    filterset_class = TaskFilter
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    filterset_fields = ['executor', 'status', 'label']


class TaskCreateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('The task has been successfully created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – create a task')
        body = {'title': _('Create a task'), 'button_value': _('create')}
        context['body'] = body
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskReadView(LoginRequiredMixinWithMessage, DetailView):
    model = Task
    template_name = 'task/read.html'
    login_url = reverse_lazy('login_view')
    context_object_name = 'task'


class TaskUpdateView(LoginRequiredMixinWithMessage, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('The task has been successfully changed')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        body = {'title': _('Change the task'), 'button_value': _('edit')}
        context['title'] = _('Task Manager – change the task')
        context['body'] = body
        return context


class TaskDeleteView(LoginRequiredMixinWithMessage, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('The task has been successfully deleted')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Task Manager – delete a task')
        context['body'] = {
            'title': _('Delete a task'),
            'subtitle': f"{_('Are you sure you want to delete the task')}: {context['task'].name}",
            'button_value': _('Yes, delete'),
        }
        return context

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task_author = Task.objects.get(id=task_id).author
        if request.user.id == task_author.id:
            return super().post(self, request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            _('Only the author of the task can delete it'),
        )
        return redirect(reverse_lazy('tasks_index'))
