from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Client

def client_list(request):
    if request.method == "GET":
      client_list = Client.objects.all()
      template_name = 'clients/list.html'
      
      context = {
        'all_clients': client_list
      }
      
      return render(request, template_name, context)
  
    elif request.method == 'POST':
        form_data = request.POST
        
        new_client = Client.objects.create(
            name = form_data['name'],
            address = form_data['address'],
            city = form_data['city'],
            state = form_data['state'],
            zipcode = form_data['zipcode'],
            company_phone_number = form_data["company_phone_number"],
            contact_first_name = form_data["contact_first_name"],
            contact_last_name = form_data["contact_last_name"],
            contact_phone_number = form_data["contact_phone_number"],
            contact_email = form_data["contact_email"],
          )


        return redirect(reverse('masterplanapp:projects'))