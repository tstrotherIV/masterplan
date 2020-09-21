from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Project, Client, Venue, HouseAV
from django.contrib.auth.models import User

def project_form(request):
    
    Client.objects.create(
            name = "",
            address = "",
            city = "",
            state = "",
            zipcode = "",
            company_phone_number = "",
            contact_first_name = "",
            contact_last_name = "",
            contact_phone_number = "",
            contact_email = "",
          )
    
    if request.method == "GET":
      client = Client.objects.latest('id')
      
    HouseAV.objects.create(
            name = "",
            contact_name = "",
            contact_email = "",
            contact_phone = "",
          )
    
    if request.method == "GET":
      houseav = HouseAV.objects.latest('id')
      
    Venue.objects.create(
            name = "",
            street_address = "",
            city = "",
            state = "",
            zipcode = "",
            contact_name = "",
            contact_email = "",
            contact_phone = "",
            onsite_parking_address = "",
            semi_parking = "",
            loading_dock = "",
            venue_phone = "",
          )
    if request.method == "GET":
      venue = Venue.objects.latest('id')
    
    Project.objects.create(
            user = request.user,
            name = '',
            description = '',
            location_name = '',
            location_address = '',
            location_city = '',
            location_state = '',
            location_zipcode = '',
            event_start_date = '0001-01-01',
            event_end_date = '0001-01-01',
            load_in_time = '',
            load_out_time = '',
            client_id = client.id,
            venue_id = venue.id,
            houseAV_id = houseav.id,
            
          )
  
    project = Project.objects.latest('id')  
    return redirect(f'/form/{project.id}')