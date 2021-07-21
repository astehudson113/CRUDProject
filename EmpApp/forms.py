from django import forms
from django import forms
from EmpApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
    


