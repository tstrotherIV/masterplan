from django.urls import path
from django.conf.urls import include
from masterplanapp import views
from .views import home, login, logout_user

app_name = "masterplanapp"

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
]