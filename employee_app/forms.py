from django import forms
from .models import Employee, Department


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            'name',
            'email',
            'salary',
            'department'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'salary': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'department': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        
class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = [
            'name',
            'location'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }