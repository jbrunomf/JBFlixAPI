from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return JsonResponse({'hello': 'world'})