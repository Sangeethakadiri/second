from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('this is first view in app1')

def app1_second(request):
    return HttpResponse('this is second view in app1')