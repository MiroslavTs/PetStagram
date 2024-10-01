# Generated by Django 5.1.1 on 2024-10-01 17:12

import PetStagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles', validators=[PetStagram.photos.validators.FileSizeValidator(5)]),
        ),
    ]
