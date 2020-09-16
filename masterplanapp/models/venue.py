from django.db import models


class Venue(models.Model):

      name = models.CharField(max_length=100, default=None, blank=True, null=True)
      street_address = models.CharField(max_length=100, default=None, blank=True, null=True)
      city = models.CharField(max_length=100, default=None, blank=True, null=True)
      state = models.CharField(max_length=100, default=None, blank=True, null=True)
      zipcode = models.CharField(max_length=100, default=None, blank=True, null=True)
      venue_phone = models.CharField(max_length=100, default=None, blank=True, null=True)
      contact_name = models.CharField(max_length=100, default=None, blank=True, null=True)
      contact_email = models.CharField(max_length=100, default=None, blank=True, null=True)
      contact_phone = models.CharField(max_length=100, default=None, blank=True, null=True)
      onsite_parking_address = models.CharField(max_length=100, default=None, blank=True, null=True)
      semi_parking = models.CharField(max_length=100, default=None, blank=True, null=True)
      loading_dock = models.CharField(max_length=100, default=None, blank=True, null=True)