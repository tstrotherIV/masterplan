from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Project


def recent_list(request):
    if request.method == "GET":
      project_list = Project.objects.filter(deleted=False, user_id=request.user)
      template_name = 'projects/recent.html'
      
      context = {
        'all_projects': project_list
      }
      
      return render(request, template_name, context)