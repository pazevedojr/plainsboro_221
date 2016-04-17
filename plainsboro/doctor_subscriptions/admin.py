from django.contrib import admin
from plainsboro.doctor_subscriptions.models import Doctor


class DoctorModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'specialization', 'address', 'neighborhood',
                    'city', 'phone', 'email']

admin.site.register(Doctor, DoctorModelAdmin)
