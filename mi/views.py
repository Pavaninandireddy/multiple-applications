from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return render(request,'rohit.html')

def Amma(request):
    return HttpResponse('<h1>I Missing you a lot ma</h1>')