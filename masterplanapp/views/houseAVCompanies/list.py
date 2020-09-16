from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import HouseAV

def houseav_list(request):
    if request.method == "GET":
      houseav_list = HouseAV.objects.all()
      template_name = 'houseAV/list.html'
      
      context = {
        'all_houseav': houseav_list
      }
      
      return render(request, template_name, context)
  
    elif request.method == 'POST':
        form_data = request.POST
        
        new_houseav = HouseAV.objects.create(
            name = form_data['name'],
            contact_name = form_data["contact_name"],
            contact_email = form_data["contact_email"],
            contact_phone = form_data["contact_phone"],
          )


        return redirect(reverse('masterplanapp:houseavs'))