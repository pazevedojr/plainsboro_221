from django.conf.urls import url
from django.contrib import admin
from plainsboro.appointments.views import doctor_details
from plainsboro.core.views import home
from plainsboro.doctor_subscriptions.views import doctor_subscribe

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^doctor_subscribe/$', doctor_subscribe),
    url(r'^doctors/(?P<slug>[\w-]+)/$', doctor_details, name='doctor_details'),
]
