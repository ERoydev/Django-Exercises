# Generated by Django 4.2.7 on 2023-12-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_pet_person_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
    ]
