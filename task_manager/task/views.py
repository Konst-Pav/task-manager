from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class TaskIndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/index.html')


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Create task')


class TaskUpdateView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Update task')


class TaskDeleteView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Delete task')

