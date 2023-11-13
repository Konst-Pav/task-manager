from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class TaskIndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/index.html')


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/create.html')


class TaskReadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'task/read.html')


class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/update.html')


class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task/delete.html')

