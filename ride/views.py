from django.shortcuts import render
from django.http import HttpResponse

def auto(request):
    return HttpResponse('<center><h1>auto are available 24/7</h1></center>')

def cab(request):
    return render(request,'cab.html')

