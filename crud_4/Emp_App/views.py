from django.shortcuts import render,redirect
from .forms import EmployeeForm
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required(login_url='Sign_In_View')
def Add_Employee_View(request):
    form = EmployeeForm()
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Employee_View')
    template_name = 'Emp_App/Add_Employee.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='Sign_In_View')
def Show_Employee_View(request):
    objs = Employee.objects.all()
    template_name = 'Emp_App/Show_Employee.html'
    context = {'records':objs}
    return render(request,template_name,context)

def Update_Employee_View(request,pk):
    obj = Employee.objects.get(emp_id = pk)
    form = EmployeeForm(instance=obj)
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Employee_View')
    template_name = 'Emp_App/Update_Employee.html'
    context = {'form':form}
    return render(request,template_name,context)

def Delete_Employee_View(request,pk):
    obj = Employee.objects.get(emp_id = pk)
    form = EmployeeForm(instance=obj)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('Show_Employee_View')
    template_name = 'Emp_App/Delete_Employee.html'
    context = {'obj':obj}
    return render(request,template_name,context)
