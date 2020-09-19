from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project

      
def project_by_priority(request):
      if request.method == "GET":
        project_list = Project.objects.filter(priority=True)
        template_name = 'projects/list.html'
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)
      
def project_by_completed(request):
      if request.method == "GET":
        project_list = Project.objects.filter(completed=True)
        template_name = 'projects/list.html'
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)
      
def project_by_confirmed(request):
      if request.method == "GET":
        project_list = Project.objects.filter(confirmed=True)
        template_name = 'projects/list.html'
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)