from django.db import models


class Venue(models.Model):

      name = models.CharField(max_length=100)
      street_address = models.CharField(max_length=100)
      city = models.CharField(max_length=100)
      state = models.CharField(max_length=100)
      zipcode = models.CharField(max_length=100)
      contact_name = models.CharField(max_length=100)
      contact_email = models.CharField(max_length=100)
      contact_phone = models.CharField(max_length=100)
      onsite_parking_address = models.CharField(max_length=100)
      semi_parking = models.CharField(max_length=100)
      loading_dock = models.CharField(max_length=100)