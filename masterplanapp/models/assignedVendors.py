from django.db import models
from .project import Project
from .vendor import Vendor


class AssignedVendor(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)