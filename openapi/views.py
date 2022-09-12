from time import sleep

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("success")


def hello(request):
    return HttpResponse("hello")


def world(request):
    return HttpResponse("world")


def login(request):
    print("logins")
    sleep(10)
    return HttpResponse("login")
