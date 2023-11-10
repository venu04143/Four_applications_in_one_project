from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'csk.html')
def raina(request):
    return HttpResponse('<h1>Most underrated player</h1>')