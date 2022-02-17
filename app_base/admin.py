from django.contrib import admin
from app_base.models import Speciality, Doctor, Reservation, Service

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Reservation)
admin.site.register(Service)