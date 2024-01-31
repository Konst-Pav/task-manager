from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredMixinWithMessage(LoginRequiredMixin):
    """ The LoginRequiredMixin extended to add a relevant message to the
    messages framework by setting the ``permission_denied_message``
    attribute. """

    login_url = '/login/'
    permission_denied_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, self.permission_denied_message)
            return self.handle_no_permission()
        return super(LoginRequiredMixinWithMessage, self).dispatch(request, *args, **kwargs)
