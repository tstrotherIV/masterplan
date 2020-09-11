from django.urls import path
from django.conf.urls import include
from masterplanapp import views
from .views import home, login, logout_user, register_user

app_name = "masterplanapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
    path('register/', register_user, name="register"),
    path('accounts/logout/', logout_user, name='logout'),
    path('', home, name='home'),
]