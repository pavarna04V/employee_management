from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Department


# HOME PAGE
def home(request):
    return render(request, 'employee_app/home.html')


# LOGIN
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'employee_app/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD
def dashboard(request):

    total_employees = Employee.objects.count()
    total_departments = Department.objects.count()

    context = {
        'total_employees': total_employees,
        'total_departments': total_departments
    }

    return render(
        request,
        'employee_app/dashboard.html',
        context
    )


# ADD EMPLOYEE
def add_employee(request):

    departments = Department.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        department_id = request.POST.get('department')

        department = Department.objects.get(id=department_id)

        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            salary=salary,
            department=department
        )

        messages.success(request, 'Employee added successfully')

        return redirect('employee_list')

    context = {
        'departments': departments
    }

    return render(
        request,
        'employee_app/add_employee.html',
        context
    )


# EMPLOYEE LIST
def employee_list(request):

    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(
        request,
        'employee_app/employee_list.html',
        context
    )


# EDIT EMPLOYEE
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    departments = Department.objects.all()

    if request.method == 'POST':

        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.salary = request.POST.get('salary')

        department_id = request.POST.get('department')

        employee.department = Department.objects.get(
            id=department_id
        )

        employee.save()

        messages.success(request, 'Employee updated')

        return redirect('employee_list')

    context = {
        'employee': employee,
        'departments': departments
    }

    return render(
        request,
        'employee_app/edit_employee.html',
        context
    )


# DELETE EMPLOYEE
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    messages.success(request, 'Employee deleted')

    return redirect('employee_list')