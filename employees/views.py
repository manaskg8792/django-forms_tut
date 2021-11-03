from django.shortcuts import render
from .forms import EmployeeForm


"""
    METHOD REQUEST
    CRUD - create, read, update, delete
    POST - creat
    GET - listing, retrieve
    PUT, PATCH - update
    DELETE - deletion
    
    2 tyoes of web apps
    1) SSR - server side rendering
    2) SPA - single page 
"""

from .models import Employee


def index(request):
    print(request.POST)

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if not form.is_valid():
            return render(request, template_name='errors.html', context={'error': form.errors})

        is_married_mapper = {
            'on': True,
            'off': False
        }

        Employee.objects.create(
            full_name=form.data['full_name'],
            username=form.data['username'],
            address=form.data['address'],
            email=form.data['email'],
            phone_number=form.data['phone_number'],
            salary=form.data['salary'],
            is_married=is_married_mapper.get(form.data['is_married'], False)
        )


    form = EmployeeForm()
    employees = Employee.objects.all()
    return render(request, template_name='index.html', context={'form': form, 'employees': employees})


