# Generated by Django 4.2.7 on 2023-12-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_employee_is_full_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('jr.', 'Junior'), ('sen', 'Senior'), ('reg', 'Regular')], default='nolevel', max_length=25),
            preserve_default=False,
        ),
    ]