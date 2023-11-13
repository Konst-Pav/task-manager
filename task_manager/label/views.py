from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class LabelIndexView(View):

    def get(self, request, *args, **kwargs):
        labels = [
            {'id': 1, 'name': 'Не важно', 'created_at': '12-02-2032'},
            {'id': 2, 'name': 'В первую очередь', 'created_at': '07-12-2030'},
            {'id': 23, 'name': 'Важно', 'created_at': '12-02-2032'},
        ]
        return render(request, 'label/index.html', {'labels': labels})


class LabelCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'label/create.html')


class LabelUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'label/update.html')


class LabelDeleteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'label/delete.html')
