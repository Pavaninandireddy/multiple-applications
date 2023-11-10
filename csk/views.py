from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd (request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1> The Indian Premier League (IPL) is an Indian professional Twenty20 (T20) cricket league established in 2008.</h1>')