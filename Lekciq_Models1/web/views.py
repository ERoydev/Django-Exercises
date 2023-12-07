from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Person
from .forms import RegisterForms


def home(request):
    return render(request, 'base.html')


def index(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department_id=3)
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
    error = None
    if request.method == "GET":
        form = RegisterForms()

    else:
        form = RegisterForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                encrypted_password = Person.set_password(password)
                Person.objects.create(
                    username=username,
                    password=encrypted_password,
                )
            else:
                error = "Passwords do not match!"
                print('mistake paswwords')

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'forms.html', context)
