from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from masterplanapp.models import Client

def client_form(request):
    if request.method == 'GET':
        template = 'formSections/clientInfo.html'
        

        return render(request, template)