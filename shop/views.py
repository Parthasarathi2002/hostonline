from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.

def home(request):
    data={
        "name":"parthasarathi",
        "number":[1,2,3,4,5,6,7,8,9,0],
        "dis":{"hi":"partha",'bey':'sarathi'}     
    }
    return render(request,"indexx.html",data)
def all(request):
    all=product.objects.all()
    return render(request,"partha.html",{'all':all})

from .models import*
def add(request):
    if request.method =='POST':
        name=request.POST.get('username')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        product.objects.create(name=name,age=age,email=email,password=password)
        return redirect('/show')
        # return HttpResponse("this login was succesufll")
    return render(request,'user.html')
def show(request):
    all=product.objects.all()
    return render(request,'show.html',{'all':all})

def delet(request,n):
    m=product.objects.get(id=n)
    m.delete()
    return redirect('/show')

def update(request,n):
    all=product.objects.get(id=n)
    if request.method=="POST":
        newname=request.POST.get('name')    
        newage=request.POST.get('age')    
        newemail=request.POST.get('email')    
        newpass=request.POST.get('pass') 
        all.name=newname 
        all.age=newage
        all.email=newemail
        all.password=newpass 
        all.save()
        return redirect('/show') 
    return render(request,'update.html',{'all':all})