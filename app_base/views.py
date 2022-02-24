from django.shortcuts import render
from django.http import JsonResponse
from app_base.models import Service


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')