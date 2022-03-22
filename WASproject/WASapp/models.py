from django.db import models
from django.utils import timezone


class Courses(models.Model):
    title = models.CharField(default=" ", max_length=128, unique=True)
    startDate = models.DateField(default=timezone.now)
    description = models.CharField(default=" ", max_length=500)

    def __str__(self):
        return self.title