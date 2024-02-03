from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.frontpage, name="frontpage"),
    path("about/", views.about, name="about"),             
    path("", include("blogBack.urls")), 
 
]