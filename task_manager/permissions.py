from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class EditingProfilePermissionMixin(AccessMixin):
    message = _("You don't have permission to change another user.")
    permission_denied_message = message

    def has_permission(self):
        return self.request.user.id == self.kwargs.get("pk")

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.add_message(
                request, messages.ERROR, self.permission_denied_message
            )
            return redirect(reverse_lazy("users_index"))
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredMixinWithMessage(LoginRequiredMixin):
    login_url = reverse_lazy("login_view")
    login_required_message = _("You are not logged in! Please log in.")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                self.login_required_message,
            )
            return self.handle_no_permission()
        return super(LoginRequiredMixinWithMessage, self).dispatch(
            request, *args, **kwargs
        )
