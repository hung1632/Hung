from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')
def phone(request):
    return render (request, 'phone.html')
def Investment(request):
    return render (request, 'Investment.html')
def Jobs(request):
    return render (request, 'Jobs.html')
def PC(request):
    return render (request, 'PC.html')
def Sports(request):
    return render (request, 'Sports.html')