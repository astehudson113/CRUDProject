from django.shortcuts import redirect,render
from EmpApp.forms import EmployeeForm
from EmpApp.models import Employee


# Create your views here.
def view1(request):
  f=EmployeeForm()
  if request.method=="POST":
     f=EmployeeForm(request.POST)
     if f.is_valid():
       f.save(commit=True)
       return redirect("/insert")
  else:
     e=Employee.objects.all()
     return render(request,'EmpApp/Output.html',{'form':f,'emp':e})

def view2(request,id):
  e=Employee.objects.get(id=id)
  if request.method=="POST":
    f=EmployeeForm()
    f=EmployeeForm(request.POST,instance=e)
    if f.is_valid():
     f.save(commit=True)
     return redirect("/insert")

  else:
     f=EmployeeForm()
     e=Employee.objects.get(id=id)
     f=EmployeeForm(instance=e)
     d={'form':e}
     return render(request,'EmpApp/Update.html',{'form':f})


def view3(request,id):
   e=Employee.objects.get(id=id)
   e.delete()
   return redirect("/insert")   

def view4(request):
  given_name=request.POST['name']
  e=Employee.objects.filter(ename__iexact=given_name) 
  return render(request,'EmpApp/Output.html',{'emp':e})

      
      
      







  
 