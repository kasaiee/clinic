from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')