from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request, 'web_app/login.html', {})

def accpage(request):
	return render(request, 'web_app/accpage.html', {})

def homepage(request):
	return render(request, 'web_app/homepage.html', {})

def payroll(request):
    return render(request, 'web_app/payroll.html', {})

def employee(request):
    return render(request, 'web_app/employee.html', {})

def dailyrep(request):
    return render(request, 'web_app/daily.html', {})