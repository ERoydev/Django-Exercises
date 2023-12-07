from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department


class NameForms(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


def home(request):
    return render(request, 'base.html')


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


def department_details(request, pk, slug):

    context = {
        'department': get_object_or_404(Department, pk=pk, slug_field=slug),
    }

    return render(request, 'department_details.html', context)


def forms_demo(request):
    context = {
        'form': NameForms(),
    }

    return render(request, 'forms.html', context)
