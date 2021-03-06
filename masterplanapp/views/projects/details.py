import json
from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, Client
from ..clients.details import client_details
from ..clients.list import client_list


@login_required
def project_details(request, project_id):
    if request.method == 'GET':
        project = Project.objects.get(pk=project_id)
        progressbar = []
        completed = []
      
        for attr, value in project.__dict__.items():
            if value == '':
                progressbar.append(attr)
            else:
                completed.append(attr)
                
        for attr, value in project.client.__dict__.items():
            if value == '':
                progressbar.append(attr)
            
                
        for attr, value in project.venue.__dict__.items():
            if value == '':
                progressbar.append(attr)
           
                
        for attr, value in project.houseAV.__dict__.items():
            if value == '':
                progressbar.append(attr)
            
        print(completed)
        # total fields is 37
        progressbar_value = int(len(progressbar))
        finished = 37 - progressbar_value
        percentage = int((finished/37)*100)
        
        template = 'projects/detail.html'
        context = {
            'project': project,
            'progressbar_value': finished,
            'percentage': percentage
        }
        
        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            project_to_update = Project.objects.get(pk=project_id)
            

            project_to_update.name = form_data['name']
            project_to_update.description = form_data['description']
            project_to_update.location_name = form_data['location_name']
            project_to_update.location_address = form_data['location_address']
            project_to_update.location_city = form_data['location_city']
            project_to_update.location_state = form_data["location_state"]
            project_to_update.location_zipcode = form_data["location_zipcode"]
            project_to_update.event_start_date = form_data["event_start_date"]
            project_to_update.event_end_date = form_data["event_end_date"]
            project_to_update.load_in_time = form_data["load_in_time"]
            project_to_update.load_out_time = form_data["load_out_time"]
            project_to_update.confirmed = form_data["confirmed"]
            project_to_update.priority = form_data["priority"]
            project_to_update.completed = form_data["completed"]
            
            project_to_update.save()
            
            return HttpResponse(project_id)
        

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
    
    