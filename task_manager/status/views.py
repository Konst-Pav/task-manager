from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class StatusIndexView(View):

    def get(self, request, *args, **kwargs):
        statuses = [
            {
                'id': 1,
                'name': 'tota',
                'created_at': '25-10-2023',
            },
            {
                'id': 2,
                'name': 'extra',
                'created_at': '27-10-2023',
            }
        ]
        return render(request, 'status/index.html', {'statuses': statuses})


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Create status')


class StatusUpdateView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Update status')


class StatusDeleteView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Delete status')
