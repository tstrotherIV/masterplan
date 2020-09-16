import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project


@login_required
def project_details(request, project_id):
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

            project_to_update.save()

            return HttpResponse(project_id)


    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):

                project_to_burn = Project.objects.get(pk=project_id)
                project_to_burn.delete()


                return redirect(reverse('masterplanapp:projects'))
    
    