from django.shortcuts import render
from .models import Student
def home(request):
    return render(request,'index.html')
def add(request):
   # email = request.GET['email']
    #password = request.GET['password']
    details = Student.objects.all()
    length=len(details)
    category = Student.objects.get(email=request.GET['email'])
   # password = Student.objects.get(password=request.GET['password'])
              
    

   
   
   
    return render(request,'result.html' ,{"category":category})

    

# Create your views here.
