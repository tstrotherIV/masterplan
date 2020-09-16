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
    path('projects/form', project_form, name='project_form'),
    path('projects/form/<int:project_id>', project_details, name='project_details'),
    path('projects/form/<int:project_id>', client_details, name='client_details'),
    path('projects/<int:project_id>/', project_details, name='project'),
    path('clients/', client_list, name='clients'),
    path('venues/', venue_list, name='venues'),
    path('houseavs/', houseav_list, name='houseavs'),
]