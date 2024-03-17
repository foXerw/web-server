from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def hello_view(request):
    data = {"test": "yoooooo"}
    return JsonResponse(data)
