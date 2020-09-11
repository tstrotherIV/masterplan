from django.db import models
from .client import Client
from .union import Union
from .houseAV import HouseAV
from .venue import Venue


class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    location_address = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    location_zipcode = models.CharField(max_length=100)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    load_in_time = models.CharField(max_length=100)
    load_out_time = models.CharField(max_length=100)
    completed = models.BooleanField()
    deleted = models.BooleanField()
    priority = models.BooleanField()
    confirmed = models.BooleanField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    union =  models.ForeignKey(Union, on_delete=models.DO_NOTHING)
    houseAV = models.ForeignKey(HouseAV, on_delete=models.DO_NOTHING)
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    
    

    def __str__(self):
        return f"{self.name}"