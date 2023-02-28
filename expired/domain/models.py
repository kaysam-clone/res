from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AllDomain(models.Model):
    domains = models.JSONField()
