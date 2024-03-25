from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        title = _('Simple and flexible task management web application')
        return render(
            request,
            'index.html',
            {'title': title}
        )
