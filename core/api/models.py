from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    activity = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    participants = models.IntegerField()
    price = models.FloatField()
    link = models.URLField(blank=True, null=True)
    key = models.CharField(max_length=255)
    accessibility = models.FloatField()
    done = models.BooleanField(default=False)