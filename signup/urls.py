from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", Signup.as_view(), name='signup'),
    path("login/", loginView, name='loginpath'),
    path("tokenpath/", tokenView, name='tokenpath'),
    path("logout/", logoutView, name='logoutpath')

]
