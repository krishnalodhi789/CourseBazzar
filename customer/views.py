from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Customer, Course


def signupform(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender =request.POST.get('gender')
        password =request.POST.get('password')
        conform_password =request.POST.get('conform_password')
        if conform_password == password :
            user = User.objects.create_user(
                username = email,
                email =email,
                first_name=first_name,
                last_name = last_name,
                password=password
            )
            user.save()
            customer =Customer.objects.create(
                user = user,
                phone = phone,
                gender = gender,
            )
            customer.save()
            return redirect('/')
        else:
            return redirect('signup')
        
    return render(request, 'signupform.html')


def customerlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = email).exists() :
            messages.error(request, 'Invalid Email and Password !!')
            return redirect('login')
        user = User.objects.get(username = email)
        # print(user.customer)
        if not Customer.objects.filter(user = user).exists() :
            messages.error(request, 'Invalid Email and Password !!')
            return redirect('login')
        customer = authenticate(username=email, password=password)
        if customer is not None:
            login(request,customer)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Email and Password !!')
            return redirect('login')
    return render(request,'loginform.html')

def customerlogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def customerprofile(request):
    return render(request, 'customerprofile.html' )


@login_required(login_url='login')
def addcourse(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        description = request.POST.get('description')
        pdf = request.FILES.get('course_file')
        image =request.FILES.get('image')
        
        customer = Customer.objects.get(user_id=request.user.id)
        course = Course.objects.create(
            customer = customer,
            title =title,
            description = description,
            price = price,
            course_file = pdf,
            image =image,
        )
        course.save()
        return redirect('uploadedcourses')
    return render(request, 'addcourse.html')

@login_required(login_url='login')
def uploadedcourses(request):
    customer = Customer.objects.get(user_id=request.user.id)
    courses = Course.objects.filter(customer_id=customer.id)
    context = {'courses':courses}
    print(courses)
    return render(request, 'uploadedcourses.html', context)