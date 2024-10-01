from django.urls import path

from PetStagram.common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
]