from django.shortcuts import render, redirect
from django.urls import reverse
from masterplanapp.models import Project, Media

def media_list(request):
    if request.method == "GET":
      media_list = Media.objects.filter(user_id=request.user)
      template_name = 'media/list.html'
      
      context = {
        'all_medias': media_list
      }
      
      return render(request, template_name, context)
  
  
    elif request.method == 'POST':
        form_data = request.POST
        
        Media.objects.create(
            name = form_data['name'],
          )

        return redirect(reverse('masterplanapp:projects'))
      
