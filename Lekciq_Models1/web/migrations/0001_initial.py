# Generated by Django 4.2.7 on 2023-12-06 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(default='IT', max_length=50)),
                ('salary', models.PositiveIntegerField(default=1500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', models.TextField(max_length=12)),
                ('level', models.CharField(choices=[('jr.', 'Junior'), ('sen', 'Senior'), ('reg', 'Regular')], default='Regular', max_length=25, verbose_name='seniority_level')),
                ('years_of_experience', models.PositiveIntegerField()),
                ('review', models.TextField(blank=True, null=True)),
                ('is_full_time', models.BooleanField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.department')),
            ],
            options={
                'ordering': ('-years_of_experience', 'age'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('code_name', models.CharField(max_length=10, unique=True)),
                ('deadline', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.employee')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.project')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ManyToManyField(related_name='employees', to='web.project'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
