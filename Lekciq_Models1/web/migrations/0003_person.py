# Generated by Django 4.2.7 on 2023-12-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_department_slug_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField()),
            ],
        ),
    ]