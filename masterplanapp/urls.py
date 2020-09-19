from django.urls import path
from django.conf.urls import include
from masterplanapp import views
from .views import *

app_name = "masterplanapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
    path('register/', register_user, name="register"),
    path('accounts/logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('projects/', project_list, name='projects'),
    path('projectsArchives/', project_archive_list, name='projectsArchives'),
    path('projectsPriority/', project_by_priority, name='projectsPriority'),
    path('projectsConfirmed/', project_by_confirmed, name='projectsConfirmed'),
    path('projectPrintOut/<int:project_id>/', project_print_out, name='projectPrintOut'),
    path('projectsCompleted/', project_by_completed, name='projectsCompleted'),
    path('projects/form/', project_form, name='project_form'),
    path('projects/<int:project_id>/', project_details, name='project'),
    path('form/<int:project_id>', project_details, name='project_details'),
    path('client/<int:client_id>/', client_details, name='client'),
    path('clients/', client_list, name='clients'),
    path('projects/<int:project_id>/', houseav_details, name='houseav'),
    path('projects/<int:project_id>/', venue_details, name='venue'),
    path('venue/<int:venue_id>', venue_details, name='venue'),
    path('venues/', venue_list, name='venues'),
    path('houseav/<int:houseav_id>', houseav_details, name='houseav'),
    path('houseavs/', houseav_list, name='houseavs'),
]