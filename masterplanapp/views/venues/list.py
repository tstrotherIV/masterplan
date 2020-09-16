from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Venue

def venue_list(request):
    if request.method == "GET":
      venue_list = Venue.objects.all()
      template_name = 'venue/list.html'
      
      context = {
        'all_venues': venue_list
      }
      
      return render(request, template_name, context)
  
    elif request.method == 'POST':
        form_data = request.POST
        
        new_venue = Venue.objects.create(
            name = form_data['name'],
            street_address = form_data['address'],
            city = form_data['city'],
            state = form_data['state'],
            zipcode = form_data['zipcode'],
            contact_name = form_data["contact_name"],
            contact_email = form_data["contact_email"],
            contact_phone = form_data["contact_phone"],
            onsite_parking_address = form_data["onsite_parking_address"],
            semi_parking = form_data["semi_parking"],
            loading_dock = form_data["loading_dock"],
            venue_phone = form_data["venue_phone"],
          )


        return redirect(reverse('masterplanapp:venues'))