# Generated by Django 4.2.7 on 2023-12-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_employee_first_name_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]
