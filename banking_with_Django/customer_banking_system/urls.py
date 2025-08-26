from django.urls import path
from . import views as this_is_customer

urlpatterns = [
    path('profile/', this_is_customer.profile,name="profile"),
]