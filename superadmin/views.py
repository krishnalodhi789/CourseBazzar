from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.models import Course


def loginform(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		superadmin = authenticate(username=username, password=password)
		print(superadmin)
		if superadmin is not None:
			login(request, superadmin)
			return redirect('superadmin_index')
		else:
			messages.error(request,"Invalid Username and Password..")
			return redirect('superadmin_loginform')
	return render(request,"superadmin/login.html")



@login_required(login_url='superadmin_loginform')
def index(request):
	return render(request,"superadmin/index.html")


@login_required(login_url='superadmin_loginform')
def approved_course_list(request):
	courselist = Course.objects.filter(approve=True)
	total_course=courselist.count()
	context={
	'courselist':courselist,
	'total_course':total_course
	}
	return render(request,"superadmin/approved_course_list.html", context)

@login_required(login_url='superadmin_loginform')
def not_approved_course_list(request):
	courselist = Course.objects.filter(approve=False)
	total_course=courselist.count()
	context={
	'courselist':courselist,
	'total_course':total_course
	}
	return render(request,"superadmin/not_approved_course_list.html", context)