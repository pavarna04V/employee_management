from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'register/',
        views.register_view,
        name='register'
    ),

    # LOGIN
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    # LOGOUT
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # DASHBOARD
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
    
    # DEPARTMENTS
    path(
        'departments/',
        views.departments,
        name='departments'
    ),
    
    path(
            'add-department/',
            views.add_department,
            name='add_department'
        ),

    # ADD EMPLOYEE
    path(
        'add-employee/',
        views.add_employee,
        name='add_employee'
    ),

    # EMPLOYEE LIST
    path(
        'employees/',
        views.employee_list,
        name='employee_list'
    ),

    # EDIT EMPLOYEE
    path(
        'edit-employee/<int:id>/',
        views.edit_employee,
        name='edit_employee'
    ),

    # DELETE EMPLOYEE
    path(
        'delete-employee/<int:id>/',
        views.delete_employee,
        name='delete_employee'
    ),

]