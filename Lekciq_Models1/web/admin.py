from django.contrib import admin
from web.models import Employee, Department, Project, Category

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'level', 'department')
    list_filter = ('level', 'department')
    search_fields = ('first_name', 'last_name')

    fieldsets= (
        ('Personal Info',
         {
             'fields': ('first_name', 'last_name', 'age', 'phone_number', 'email'),
         }
         ),
        ('Advanced options',
         {
             'fields': ('level', 'years_of_experience'),
         }
         ),

        ('Company Info',
        {
            'fields': ('department', 'is_full_time',),
        }
        )
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'salary')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
