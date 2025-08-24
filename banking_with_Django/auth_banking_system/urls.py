from django.urls import path
from . import views as this_is_auth

urlpatterns = [
    path('',this_is_auth.home, name='home'),
    path('contact/',this_is_auth.contact, name='contact'),
    path('about/',this_is_auth.about, name='about_us'),
    path('signin/',this_is_auth.signin, name='signin'),
    path('signup/',this_is_auth.signup, name='signup'),
]