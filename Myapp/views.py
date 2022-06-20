from django.shortcuts import render
from django.http import HttpResponse
from Myapp.models import Contact

# Create your views here.
def dashboard(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')
def video(request):
    return render(request,'video.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        values=Contact(name=name,email=email,desc=desc)
        values.save()
    return render(request,'contact.html')