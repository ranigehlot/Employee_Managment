from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import Employee

# Create your views here.

def add(request):
    empform=EmpForm
    return render(request,'add.html',{'empform':empform})

def insert(request):
    if request.method=="POST":
        empform=EmpForm(request.POST)
        if empform.is_valid:
            empform.save()
            return redirect('signin')
        else:
            return redirect('add')
    else:
        return redirect('add')        
def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees}) 

def edit(request,eid):
    emp =Employee.objects.get(eid=eid) 
    return render(request,'edit.html',{'emp':emp})   

def update(request,eid):
    if request.method=="POST":
        emp=Employee.objects.get(eid=eid)
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect("show") 
        else:
            return render(request,'edit.html',{'emp':emp})      
    else:
            return render(request,'edit.html',{'emp':emp})         
        
def delete(request,eid):
    emp=Employee.objects.get(eid=eid) 
    emp.delete()
    return redirect('show')
        
