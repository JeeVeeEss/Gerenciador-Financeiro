from django.shortcuts import render
from django.http import HttpResponse # módulo para realizar respostas em http.

def index(request):
    return  HttpResponse("Nice!")