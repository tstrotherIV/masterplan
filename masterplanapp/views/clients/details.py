import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, Client


@login_required
def client_details(request, client_id):
    if request.method == 'GET':
        client = Client.objects.get(pk=client_id)

        template = 'projects/detail.html'
        context = {
            'client': client
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            client_to_update = Project.objects.get(pk=client_id)

            client_to_update.name = form_data['name']
            client_to_update.address = form_data['address']
            client_to_update.city = form_data['city']
            client_to_update.state = form_data['state']
            client_to_update.zipcode = form_data['zipcode']
            client_to_update.company_phone_number = form_data["company_phone_number"]
            client_to_update.contact_first_name = form_data["contact_first_name"]
            client_to_update.contact_last_name = form_data["contact_last_name"]
            client_to_update.contact_phone_number = form_data["contact_phone_number"]
            client_to_update.contact_email = form_data["contact_email"]

            client_to_update.save()

            return HttpResponse(client_id)


    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):

                client_to_burn = Client.objects.get(pk=client_id)
                client_to_burn.delete()


                return redirect(reverse('masterplanapp:projects'))