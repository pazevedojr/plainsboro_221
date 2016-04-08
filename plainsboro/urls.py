from django.conf.urls import url
from django.contrib import admin
from plainsboro.core.views import home, doctor_details

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^doctors/(?P<slug>[\w-]+)/$', doctor_details,
        name='doctor_details')
]
