from django.db import models

class Vendor(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    