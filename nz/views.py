from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def kane(request):
    return HttpResponse("<h1>century</h1>")

def convae(request):
    return HttpResponse("<h1>A Century</h1>")