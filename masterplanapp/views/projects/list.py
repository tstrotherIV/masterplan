from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Client, HouseAV, Union, Venue, Project

def project_list(request):
    if request.method == "GET":
      project_list = Project.objects.filter(deleted=False, user_id=request.user)
      template_name = 'projects/list.html'
      
      context = {
        'all_projects': project_list
      }
      
      return render(request, template_name, context)
  
  
    elif request.method == 'POST':
        form_data = request.POST
        
        Project.objects.create(
            name = form_data['name'],
            description = form_data['description'],
            location_name = form_data['location_name'],
            location_address = form_data['location_address'],
            location_city = form_data['location_city'],
            location_state = form_data["location_state"],
            location_zipcode = form_data["location_zipcode"],
            event_start_date = form_data["event_start_date"],
            event_end_date = form_data["event_end_date"],
            load_in_time = form_data["load_in_time"],
            load_out_time = form_data["load_out_time"],
          )

        return redirect(reverse('masterplanapp:projects'))
      
def project_archive_list(request):
    if request.method == "GET":
      project_list = Project.objects.filter(deleted=True, user_id=request.user)
      template_name = 'archivedProjects/list.html'
      
      context = {
        'all_projects': project_list
      }
      
      return render(request, template_name, context)
    
def recent_list(request):
    if request.method == "GET":
      project_list = Project.objects.filter(deleted=False, user_id=request.user)
      template_name = 'projects/recent.html'
      
      context = {
        'all_projects': project_list
      }
      
      return render(request, template_name, context)