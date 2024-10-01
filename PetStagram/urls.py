
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PetStagram.common.urls')),
    path('accounts/', include('PetStagram.accounts.urls')),
    path('pets/', include('PetStagram.pets.urls')),
    path('photos/', include('PetStagram.photos.urls')),
]
