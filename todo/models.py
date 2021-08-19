from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    task_complete = models.BooleanField(default=False)
    completion_date = models.DateTimeField(blank=True, null=True)
    task_archived = models.BooleanField(default=False)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
