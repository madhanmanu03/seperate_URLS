from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse("<h1>50tha vathu century</h1>")

def shresh(request):
    return HttpResponse("<h1>Had a Century</h1>")