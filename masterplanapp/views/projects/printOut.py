from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Client, HouseAV, Union, Venue, Project

def project_print_out(request, project_id):
    if request.method == 'GET':
        project = Project.objects.get(pk=project_id)
        
        template = 'printOut/printOutSections/MasterPrintOut.html'
        context = {
            'project': project
        }
        
        return render(request, template, context)