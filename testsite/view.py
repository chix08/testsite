from django.http import HttpResponse

from django.shortcuts import render
#
# from django.db import models

def home(request):

    response = HttpResponse()
    response.write("<h1>Hello world</h1>")
    return response


