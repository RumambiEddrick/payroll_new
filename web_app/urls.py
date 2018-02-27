from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^home$', views.homepage, name='homepage'),
    url(r'^account$', views.accpage, name='accpage'),
    url(r'^payroll$', views.payroll, name='payroll'),
    url(r'^member$', views.member, name='member'),
]