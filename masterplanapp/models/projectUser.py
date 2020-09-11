from django.db import models
from .project import Project
from django.contrib.auth.models import User


class ProjectUser(models.Model):
    
    confirmed = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)