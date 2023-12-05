from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department


def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department_id=2)
    employees3 = Employee.objects.filter(department__role='Engineering')
    context = {
        'employees': employees,
        'employees2': employees2,
        'employees3': employees3,
    }
    return render(request, 'index.html', context)


def delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')