from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Department
from django.contrib.auth.models import User
from .forms import DepartmentForm

# HOME PAGE
def home(request):
    return render(request, 'employee_app/home.html')

# REGISTER
def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # auto login after register
        login(request, user)

        messages.success(request, 'Registration successful')

        return redirect('dashboard')

    return render(request, 'employee_app/register.html')

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

# DEPARTMENTS
def departments(request):

    departments = Department.objects.all()

    context = {
        'departments': departments
    }

    return render(
        request,
        'employee_app/departments.html',
        context
    )
    
# ADD DEPARTMENT
def add_department(request):

    form = DepartmentForm()

    if request.method == 'POST':

        form = DepartmentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Department added successfully'
            )

            return redirect('departments')

    context = {
        'form': form
    }

    return render(
        request,
        'employee_app/add_department.html',
        context
    )
# ADD EMPLOYEE
# def add_employee(request):

#     departments = Department.objects.all()

#     if request.method == 'POST':

#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         salary = request.POST.get('salary')
#         department_id = request.POST.get('department')

#         department = Department.objects.get(id=department_id)

#         Employee.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             salary=salary,
#             department=department
#         )

#         messages.success(request, 'Employee added successfully')

#         return redirect('employee_list')

#     context = {
#         'departments': departments
#     }

#     return render(
#         request,
#         'employee_app/add_employee.html',
#         context
#     )

from django.core.mail import send_mail
from django.conf import settings

def add_employee(request):

    departments = Department.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        department_id = request.POST.get('department')

        department = Department.objects.get(id=department_id)

        employee = Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            salary=salary,
            department=department
        )

        # 📧 SMTP EMAIL SEND
        send_mail(
            subject="Welcome to Company 🎉",
            message=f"""
Hi {employee.name},

Your employee account has been created successfully.

Department: {employee.department.name}
Salary: {employee.salary}

Welcome to the team!

Regards,
HR Team
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[employee.email],
            fail_silently=False,
        )

        messages.success(request, "Employee added successfully & Email sent")

        return redirect('employee_list')

    return render(request, 'employee_app/add_employee.html', {
        'departments': departments
    })


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