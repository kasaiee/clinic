from django.shortcuts import render
from django.http import JsonResponse
from app_base.models import Service
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


@api_view()
def service_list(request):
    """
    Display all `services`
    """
    service_list = Service.objects.all()
    serializer = ServiceSerializer(service_list, many=True)
    return Response(serializer.data)

# def service_list(request):
#     service_list = Service.objects.all()
#     data = []
#     for service in service_list:
#         data.append({
#             'name': service.name
#         })
#     return JsonResponse(data, safe=False)


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')