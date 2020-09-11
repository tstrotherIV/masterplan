from django.db import models

class Client(models.Model):
  
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_phone_number =  models.CharField(max_length=100)
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_pohone_number = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}, {self.contact_first_name}, {self.contact_last_name}"