from django.contrib import admin
from EmpApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
   L=['eid','ename','email','ephno','eexp','edob','esal']

admin.site.register(Employee,EmployeeAdmin)
