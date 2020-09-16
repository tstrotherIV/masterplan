from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Venue

def venue_form(request):
    if request.method == 'GET':
        template = 'formSections/venueInfo.html'
        

        return render(request, template)