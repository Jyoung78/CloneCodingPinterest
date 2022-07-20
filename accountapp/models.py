from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.views.generic import CreateView

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
