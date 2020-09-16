import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, Venue


@login_required
def venue_details(request, venue_id):
    if request.method == 'GET':
        venue = Venue.objects.get(pk=venue_id)

        template = 'venues/detail.html'
        context = {
            'venue': venue
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            venue_to_update = Venue.objects.get(pk=venue_id)

            venue_to_update.name = form_data['name']
            venue_to_update.street_address = form_data['address']
            venue_to_update.city = form_data['city']
            venue_to_update.state = form_data['state']
            venue_to_update.zipcode = form_data['zipcode']
            venue_to_update.contact_name = form_data["contact_name"]
            venue_to_update.contact_email = form_data["contact_email"]
            venue_to_update.contact_phone = form_data["contact_phone"]
            venue_to_update.onsite_parking = form_data["onsite_parking"]
            venue_to_update.onsite_parking = form_data["onsite_parking"]
            venue_to_update.semi_parking = form_data["semi_parking"]
            venue_to_update.loading_dock = form_data["loading_dock"]
            venue_to_update.venue_phone = form_data["venue_phone"]

            venue_to_update.save()

            return HttpResponse(venue_id)


    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):

                venue_to_burn = Venue.objects.get(pk=venue_id)
                venue_to_burn.delete()


                return redirect(reverse('masterplanapp:venues'))