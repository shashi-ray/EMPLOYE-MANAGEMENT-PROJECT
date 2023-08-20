from django.shortcuts import render
from .models import Employe
from django.http import HttpResponse

# Create your views here.
def HOME_VIEW(request):
    return render(request,'home.html')
def ABOUT_VIEW(request):
    return render(request,'about.html')
def CONTACT_VIEW(request):
    return render(request,'contact.html')
def VIEW_ALL(request):
    emp=Employe.objects.all()
    return render(request,'view.html',context={'emps':emp})
def ADD_EMPLOYE(request):
    if request.method=='POST':
        name=request.POST['name']
        salary=int(request.POST['salary'])
        dept=request.POST['dept']
        role=request.POST['role']
        emp=Employe(name=name,salary=salary,dept=dept,role=role)
        emp.save()
        return render(request,'addedsucces.html')
    else:
        return render(request,'add.html')
def REMOVE_EMP(request,id=0):
    if id:
        try:
            emp_to_remove=Employe.objects.get(id=id)
            emp_to_remove.delete()
            return HttpResponse('<h4>employe deleted sucessfully</h4>')
        except:
            return HttpResponse('<h1>please selct valid employe id</h1>')
    emp=Employe.objects.all()
    context={'emps':emp}
    return render(request,'remove.html',context)
def FILTER_EMP(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        salary=request.POST['salary']
        emps=Employe.objects.all()
        if name:
            emps=emps.filter(name__icontains=name)
        if dept:
            emps=emps.filter(dept__icontains=dept)
        if role:
            emps=emps.filter(role__icontains=role)
        if salary:
            emps=emps.filter(salary=salary)
        context={'emps':emps}
        return render(request,'view.html',context)
    elif request.method=='GET':
        return render(request,'filter.html')
    else:
        return HttpResponse('not valid employe')
def UPDATE_EMP(request,id=0):
    if id:
        emps=Employe.objects.get(id=id)
        context={'emps':emps}
        return render(request,'update.html',context)

def UPDATE_EMPLOYE(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        salary=int(request.POST.get('salary'))
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        emp=Employe.objects.get(id=id)
        emp.name=name
        emp.salary=salary
        emp.dept=dept
        emp.role=role
        emp.save()
        
        return HttpResponse('employe updated')
    else:
        return render(request,'home.html')