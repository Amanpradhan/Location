from django.conf.urls import url
from django.contrib import admin
from location import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^request_access/$', views.request_access,
        name='request_access'),
]
