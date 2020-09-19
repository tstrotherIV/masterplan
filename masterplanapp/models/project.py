from django.db import models
from .client import Client
from .union import Union
from .houseAV import HouseAV
from .venue import Venue


class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    location_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    location_address = models.CharField(max_length=100, default=None, blank=True, null=True)
    location_city = models.CharField(max_length=100, default=None, blank=True, null=True)
    location_state = models.CharField(max_length=100, default=None, blank=True, null=True)
    location_zipcode = models.CharField(max_length=100, default=None, blank=True, null=True)
    event_start_date = models.DateField(default='0001-01-01')
    event_end_date = models.DateField(default='0001-01-01')
    load_in_time = models.CharField(max_length=100, default=None, blank=True, null=True)
    load_out_time = models.CharField(max_length=100, default=None, blank=True, null=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    union =  models.ForeignKey(Union, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    houseAV = models.ForeignKey(HouseAV, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"