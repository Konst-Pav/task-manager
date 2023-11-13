from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class UserIndexView(View):

    def get(self, request, *args, **kwargs):
        users = [{
            'id': 1,
            'nickname': 'Igogo',
            'first_name': 'Natan',
            'last_name': 'Petrov',
            'created_at': '12-02-1989'
        },
            {
                'id': 2,
                'nickname': 'Zxozx',
                'first_name': 'Petr',
                'last_name': 'Sidorov',
                'created_at': '23-11-1899'
            },
        ]
        return render(request, 'user/index.html', {'users': users})


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user/create.html')


class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user/update.html')


class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'user/delete.html')
