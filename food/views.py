from django.shortcuts import render

from django.http import HttpResponse

def veg(request):
    return HttpResponse('<center><h1>vegetarians are like goats, they will eat only plants</h1></center>')

def nonVeg(request):
    return render(request,'nonVeg.html')
