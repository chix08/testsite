from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import PostModel

def post_model_list(request):

    qs = PostModel.objects.all()
    print(qs)
    return HttpResponse("some data")