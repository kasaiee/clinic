from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_base.api.serializers import ServiceSerializer, SpecialitySerializer
from app_base.models import Service, Speciality, Appointment, Doctor
from datetime import datetime
import re
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user and user.is_authenticated and user.is_active:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'token': ''})


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

@api_view()
def speciality_list(request):
    speciality_list = Speciality.objects.all()
    serializer = SpecialitySerializer(speciality_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def appointment_add(request):
    # import pdb; pdb.set_trace()
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    appointmentDate = request.POST.get('date')
    try:
        appointment_date = datetime.strptime(appointmentDate, '%Y-%m-%d')
        assert appointment_date > datetime.now()
    except ValueError:
        return Response({
            'status': 'error',
            'statusCode': 400,
            'message': 'Invalid date!'
        })
    except AssertionError:
        return Response({
            'status': 'error',
            'statusCode': 400,
            'message': 'You should choose another date in the future!'
        })
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_is_valid = re.fullmatch(email_pattern, email)
    if not email_is_valid:
        return Response({
            'status': 'error',
            'statusCode': 400,
            'message': 'Invalid email!'
        })
    phone_pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    phone_is_valid = phone_pattern.match(phone)
    if not phone_is_valid:
        return Response({
            'status': 'error',
            'statusCode': 400,
            'message': 'Invalid phone number!'
        })

    

    speciality_id = request.POST.get('specialityId')
    speciality = Speciality.objects.get(id=speciality_id)
    
    doctor_id = request.POST.get('doctorId')
    doctor = Doctor.objects.get(id=doctor_id)

    appointment = Appointment.objects.create(
        user=request.user,
        name=name,
        phone=phone,
        email=email,
        date=appointmentDate,
        speciality=speciality,
        doctor=doctor
    )
    return Response({
        'status': 'ok',
        'statusCode': 201,
        'message': 'Appointment created successfully.'
    })

    # speciality_list = Speciality.objects.all()
    # serializer = SpecialitySerializer(speciality_list, many=True)
    # return Response(serializer.data)