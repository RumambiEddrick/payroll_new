from django.shortcuts import render
from .models import Post

# Create your views here.
def login(request):
	return render(request, 'web_app/login.html', {})

def accpage(request):
	return render(request, 'web_app/accpage.html', {})

def homepage(request):
	return render(request, 'web_app/homepage.html', {})

def payroll(request):
    return render(request, 'web_app/payroll.html', {})

def member(request):
    return render(request, 'web_app/member.html', {})