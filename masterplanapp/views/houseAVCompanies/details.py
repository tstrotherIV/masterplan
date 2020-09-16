import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, HouseAV


@login_required
def houseav_details(request, houseav_id):
    if request.method == 'GET':
        houseav = HouseAV.objects.get(pk=houseav_id)

        template = 'houseavs/detail.html'
        context = {
            'houseav': houseav
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            houseav_to_update = HouseAV.objects.get(pk=houseav_id)

            houseav_to_update.name = form_data['name']
            houseav_to_update.contact_name = form_data["contact_name"]
            houseav_to_update.contact_email = form_data["contact_email"]
            houseav_to_update.contact_phone = form_data["contact_phone"]

            houseav_to_update.save()

            return HttpResponse(houseav_id)


    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):

                venue_to_burn = HouseAV.objects.get(pk=houseav_id)
                venue_to_burn.delete()


                return redirect(reverse('masterplanapp:houseavs'))