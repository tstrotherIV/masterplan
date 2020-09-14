from django.shortcuts import render
from masterplanapp.models import Client, HouseAV, Union, Venue, Project

def project_list(request):
    project_list = Project.objects.all()
    template_name = 'projects/list.html'
    
    context = {
      'all_projects': project_list
    }
    
    return render(request, template_name, context)