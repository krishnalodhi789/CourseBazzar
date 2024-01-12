from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Customer, Course, AddToCart, AmountTransitionHistory


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
    return render(request, 'uploadedcourses.html', context)



@login_required(login_url='login')
def addtocart(request, id):
    backurl = request.META.get("HTTP_REFERER")
    customer = Customer.objects.get(user_id=request.user.id)
    course = Course.objects.get(id=id)
    
    if AddToCart.objects.filter(customer=customer,course=course).exists():
        messages.error(request,"True")
        print("already Added...")
        return redirect(backurl)
    addtocart = AddToCart.objects.create(
        customer = customer,
        course = course
    )
    addtocart.save()
    return redirect(backurl)
    
    
@login_required(login_url='login')
def customercart(request):
    customer = Customer.objects.get(user_id=request.user.id)
    carts = AddToCart.objects.filter(customer_id=customer.id)
    context = {'carts':carts}
    return render(request, 'customercart.html', context)

@login_required(login_url='login')
def deletecart(request, id):
    course = AddToCart.objects.get(id=id)
    course.delete()
    return redirect("customercart")


@login_required(login_url='login')
def wallet(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        old_balance = request.user.wallet.balance
        total_balance = old_balance+float(amount)
        new_balance = request.user.wallet
        new_balance.balance = total_balance
        new_balance.save()
        
        transition = AmountTransitionHistory.objects.create(
            user= request.user,
            status = 'credit',
            amount = amount            
        )
        transition.save()
        return redirect("wallet")
    transitions=request.user.amounttransitionhistory.all()
    print(transitions)
    context={
        'transitions':transitions
    }
    return render(request, 'wallet.html', context)

# @login_required(login_url='login')