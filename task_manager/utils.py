from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib import messages


class ProtectedErrorHandlerMixin:
    error_message = ''
    redirect_url = ''

    def post(self, request, *args, **kwargs):
        try:
            return super().post(self, request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(
                request,
                messages.ERROR,
                self.error_message,
            )
            return redirect(self.redirect_url)
