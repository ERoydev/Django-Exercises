# Generated by Django 4.2.7 on 2023-12-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
    ]
