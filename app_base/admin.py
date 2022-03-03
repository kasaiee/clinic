from django.contrib import admin
from app_base.models import Speciality, Doctor, Appointment, Service, Subscriber


@admin.action(description='Mark selected appointments as accepted')
def make_accepted(modeladmin, request, queryset):
    queryset.update(accepted=True)


class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date', 'accepted', 'doctor', 'speciality')
    list_display = ('name', 'accepted', 'date', 'doctor', 'get_doctor_phone', 'speciality')
    list_editable = ('date', )
    actions = [make_accepted]


    def get_doctor_phone(self, obj):
        return obj.doctor.phone
    
    get_doctor_phone.short_description = 'Doctor phone'


admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Service)
admin.site.register(Subscriber)