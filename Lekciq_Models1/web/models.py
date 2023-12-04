from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30)

    code_name = models.CharField(
        max_length=10,
        unique=True,
    )

    deadline = models.DateField()

    def __str__(self):
        return f"{self.name} with Deadline: {self.deadline}"


class Department(models.Model):

    role = models.CharField(
        max_length=50,
        default='IT'
    )

    salary = models.PositiveIntegerField(
        default=1500
    )

    def __str__(self):
        return f"{self.role}"


class Employee(models.Model):
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

    review = models.TextField()

    is_full_time = models.BooleanField(
        null=True
    )

    start_date = models.DateField()

    email = models.EmailField(
        unique=True,
        editable=False,
    )

    age = models.IntegerField()

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

    project = models.ManyToManyField(
        to=Project,
        related_name='employees',
    )

    def __str__(self):
        return f"Id: {self.id} Name: {self.first_name} {self.last_name}"


class AccessCard(models.Model):
    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
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
