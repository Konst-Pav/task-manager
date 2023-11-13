from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class StatusIndexView(View):

    def get(self, request, *args, **kwargs):
        statuses = [
            {
                'id': 1,
                'name': 'В процессе',
                'created_at': '25-10-2023',
            },
            {
                'id': 2,
                'name': 'На стопе',
                'created_at': '27-10-2023',
            }
        ]
        return render(request, 'status/index.html', {'statuses': statuses})


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'status/create.html')


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'status/update.html')


class StatusDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'status/delete.html')
