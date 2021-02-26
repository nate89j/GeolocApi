from django.db import models
class Creds(models.Model):
    dummy_username = models.CharField(max_length=200)
    dummy_password = models.CharField(max_length=200)
