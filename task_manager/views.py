from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        greetings = _('Hello world!')
        title = _('Hexlet Task Manager')
        return render(request, 'index.html', {'greetings': greetings, 'title': title})
