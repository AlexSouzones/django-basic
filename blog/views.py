from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("Meu blog atual")


def exemplo(request):
    return HttpResponse("Meu exemplo atual")


# Create your views here.
