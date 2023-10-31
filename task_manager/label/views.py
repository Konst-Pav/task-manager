from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class LabelIndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'label/index.html')


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Create label')


class LabelUpdateView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Update label')


class LabelDeleteView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Delete label')
