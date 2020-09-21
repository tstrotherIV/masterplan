import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, Client
from ..clients.details import client_details


@login_required
def archived_project_details(request, project_id):
    if request.method == 'GET':
        project = Project.objects.get(pk=project_id)
        
        
        template = 'projects/detail.html'
        context = {
            'project': project
        }
        
        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "ARCHIVE"
            ):

                project_to_archive = Project.objects.get(pk=project_id)
                project_to_archive.deleted = True
                
                project_to_archive.save()


                return redirect(reverse('masterplanapp:projects'))
            
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "RESTORE"
            ):

                project_to_restore = Project.objects.get(pk=project_id)
                project_to_restore.deleted = False
                
                project_to_restore.save()


                return redirect(reverse('masterplanapp:projectsArchives'))
            
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "NUKE"
            ):

                project_to_delete = Project.objects.get(pk=project_id)
                project_to_delete.delete()


                return redirect(reverse('masterplanapp:projects'))
    
    