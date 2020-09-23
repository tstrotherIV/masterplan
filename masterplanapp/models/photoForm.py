from django.forms import ModelForm
from django.db import models      
from .photo import Photo

class PhotoForm(ModelForm):
    model = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)