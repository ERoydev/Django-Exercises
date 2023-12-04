from django.contrib import admin
from web.models import Employee, Department

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass