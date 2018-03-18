from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^account$', views.accpage, name='accpage'),
    url(r'^payroll$', views.payroll, name='payroll'),
    url(r'^employee$', views.employee, name='employee'),
    url(r'^action_page.php$', views.accpage, name='accpage'),
]