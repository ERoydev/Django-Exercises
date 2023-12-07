from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import hashlib

# Create your models here.


class Person(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField()

    @staticmethod
    def set_password(password):
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hash_password = hash_object.hexdigest()
        return hash_password



class AuditInfoMixin(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)

    code_name = models.CharField(
        max_length=10,
        unique=True,
    )

    deadline = models.DateField()

    def __str__(self):
        return f"{self.name} with Deadline: {self.deadline}"


class Department(AuditInfoMixin, models.Model):

    slug_field = models.CharField(max_length=1000, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug_field:
            self.slug_field = slugify(self.role)

        return super().save(*args, **kwargs)

    role = models.CharField(
        max_length=50,
        default='IT'
    )

    salary = models.PositiveIntegerField(
        default=1500
    )

    def __str__(self):
        return f"Role: {self.role} Salary: {self.salary}"

    def get_absolute_url(self):
        return reverse('department_details', kwargs={
            'pk': self.pk,
            'slug': self.slug_field,

    })

class Employee(AuditInfoMixin, models.Model):

    class Meta:
        ordering = ('-years_of_experience', 'age')

    first_name = models.CharField(max_length=60)

    last_name = models.CharField(max_length=60)

    phone_number = models.TextField(max_length=12)

    level = models.CharField(
        max_length=25,
        choices=(
            ('jr.', 'Junior'),
            ('sen', 'Senior'),
            ('reg', 'Regular'),
        ),
        default='Regular',
        verbose_name='seniority_level',
    )

    years_of_experience = models.PositiveIntegerField()

    review = models.TextField(
        null=True, blank=True,
    )

    is_full_time = models.BooleanField(
        null=True
    )

    email = models.EmailField(
        unique=True,
    )

    age = models.IntegerField()

    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

    project = models.ManyToManyField(
        to=Project,
        related_name='employees',
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Id: {self.id} Name: {self.first_name} {self.last_name}"


class AccessCard(models.Model):
    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        to='Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


class EmployeeProject(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)

    date_joined = models.DateField(auto_now_add=True)
