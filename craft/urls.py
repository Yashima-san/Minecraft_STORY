from django.urls import path
from craft_story import views
 
urlpatterns = [
    path("home/", views.index),
    path("about/", views.about),
    path("contacts/", views.contacts),
]
