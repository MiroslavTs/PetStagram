from django.db import models
from django.core.validators import MinLengthValidator

from PetStagram.pets.models import Pet
from PetStagram.photos.validators import FileSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=(
            FileSizeValidator(5),
        )
    )

    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now_add=True
    )

