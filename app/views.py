from email.mime import image
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'the/baabtra.html')
def blog(request):
    return render(request,'the/blog.html')
def login(request):
    return render(request,'the/login.html')
def aboutus(request):
    return render(request,'the/aboutus.html')
def placement(request):
    return render(request,'the/placement.html')      
def anwer(request):
    return render(request, 'anwer.html')  



