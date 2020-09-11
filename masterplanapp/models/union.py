from django.db import models


class Union(models.Model):

      name = models.CharField(max_length=100)
      contact_name = models.CharField(max_length=100)
      contact_email = models.CharField(max_length=100)
      contact_phone = models.CharField(max_length=100)
      