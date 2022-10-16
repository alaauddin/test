from unicodedata import name
from django.shortcuts import render
from .models import User, Teacher
# Create your views here.

def home(request):
    request.method == 'POST'
    name = User.objects.first()
    age=int(20)
    pict = request.FILES.get('myfile')
    print (name, age, pict)
    newdoc = Teacher(
        name=name,
        age=age,
        pict=pict
    )

    newdoc.save()
    return render(request,'index.html')
    #return render (request,'index.html',context={}

def teachers(request):
    teacher= Teacher.objects.all()
    return render(request, "teachers.html", {'teacher':teacher})