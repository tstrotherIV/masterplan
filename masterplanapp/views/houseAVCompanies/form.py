from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from masterplanapp.models import HouseAV

def houseav_form(request):
    if request.method == 'GET':
        template = 'formSections/houseAVInfo.html'
        

        return render(request, template)