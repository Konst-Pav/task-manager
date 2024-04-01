from django.db import models
from django.contrib.auth.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    executor = models.ForeignKey(
        User,
        related_name='executor',
        on_delete=models.PROTECT,
        null=True,
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.PROTECT,
        null=True,
    )
    labels = models.ManyToManyField(Label)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager
