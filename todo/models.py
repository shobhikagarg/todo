from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = (
  (2, 'Normal'),
  (3, 'High'),
)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date =models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title