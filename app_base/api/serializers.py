from rest_framework import serializers
from app_base.models import Doctor, Service, Speciality


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    doctor_list = serializers.SerializerMethodField()

    def get_doctor_list(self, obj):
        doctor_list = obj.doctor_set.all()
        serializer = DoctorSerializer(doctor_list, many=True)
        return serializer.data

    class Meta:
        model = Speciality
        fields = '__all__'