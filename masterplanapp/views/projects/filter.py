from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project

useThisTemplate = 'projects/list.html'

def project_by_priority(request):
      if request.method == "GET":
        project_list = Project.objects.filter(priority=True, deleted=False)
        template_name = useThisTemplate
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)
      
def project_by_completed(request):
      if request.method == "GET":
        project_list = Project.objects.filter(completed=True, deleted=False)
        template_name = useThisTemplate
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)
      
def project_by_confirmed(request):
      if request.method == "GET":
        project_list = Project.objects.filter(confirmed=True, deleted=False)
        template_name = useThisTemplate
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)
      
def project_by_date(request):
      if request.method == "GET":
        project_list = Project.objects.filter(deleted=False).order_by('event_start_date')
        template_name = useThisTemplate
        
        context = {
          'all_projects': project_list
        }
        
        return render(request, template_name, context)