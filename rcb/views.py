from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return render(request,'virat.html')
def abd(request):
    return HttpResponse('<center><h1>Mr 360</h1></center>')