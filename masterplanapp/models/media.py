from django.db import models
from .project import Project

class Media(models.Model):

      name = models.CharField(max_length=100)
      project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
      