from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import  Course, AddToCart, AmountTransitionHistory, DataHistory, CustomUser, Wallet


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
            user = CustomUser.objects.create_user(
                username = email,
                email =email,
                first_name=first_name,
                last_name = last_name,
                password=password,
                phone = phone,
                gender = gender,
            )
            user.save()
            user_wallet = Wallet.objects.create(
                user = user
            )
            return redirect('/')
        else:
            messages.error(request, 'Password and Conform Password is not same.')
            return redirect('signup')
        
    return render(request, 'signupform.html')


def customerlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

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
        
        customer = CustomUser.objects.get(id=request.user.id)
        course = Course.objects.create(
            user = customer,
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
    # customer = CustomUser.objects.get(id=request.user.id)
    approve_courses = Course.objects.filter(user_id=request.user.id,approve=True)
    not_approve_courses = Course.objects.filter(user_id=request.user.id,approve=False)
    print(not_approve_courses)
    context = {'approve_courses':approve_courses,
               'not_approve_courses':not_approve_courses,
               }
    return render(request, 'uploadedcourses.html', context)



@login_required(login_url='login')
def addtocart(request, id):
    backurl = request.META.get("HTTP_REFERER")
    user = CustomUser.objects.get(id=request.user.id)
    course = Course.objects.get(id=id)
    
    if AddToCart.objects.filter(user=user,course=course).exists():
        messages.error(request,"This course is already exist in your cart.")
        print("already Added...")
        return redirect(backurl)
   
    addtocart = AddToCart.objects.create(
        user = user,
        course = course
    )
    addtocart.save()
    return redirect(backurl)
    
    
@login_required(login_url='login')
def customercart(request):
    user = CustomUser.objects.get(id=request.user.id)
    carts = AddToCart.objects.filter(user_id=user.id)
 
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
        status = request.POST.get('status')
        wallet = request.user.wallet
        if float(amount)<0:
            messages.error(request, 'Deposit Amount should be greater than 0.')
            return redirect("wallet")
        if status == 'deposit' :
            total_balance = wallet.balance+float(amount)
            wallet.balance = total_balance
        else:
            if wallet.balance > float(amount):
                total_balance = wallet.balance-float(amount)
                wallet.balance = total_balance
            else:
                messages.error(request, 'Insufficient Balance...')
                return redirect("wallet")
        wallet.save()
        transition = AmountTransitionHistory.objects.create(
            user= request.user,
            status = status,
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

@login_required(login_url='login')
def conformorder(request):
    courses =  request.user.carts.all()
    total_price =0
    for cart in courses :
        total_price += cart.course.price
    context={
        'courses':courses,
        'total_price':total_price
    }
    return render(request, 'conformorder.html',context)


@login_required(login_url='login')
def conformation(request):
    if request.method == "POST":
        total_amount = request.POST.get('total_amount')
        user_balance = request.user.wallet
        if user_balance.balance < float(total_amount):
            messages.error(request, 'Insufficient Balance..')
            return redirect("conformorder")
        user_balance.balance -= float(total_amount)
        user_balance.save()
        superadmin = CustomUser.objects.get(username='admin')
        carts =request.user.carts.all()
        pdf_urls =[]
        for cart in carts:
            publisher = cart.course.user.wallet
            publisher.balance += cart.course.price*95/100
            superadmin.wallet.balance += cart.course.price*5/100
            publisher.save()
            superadmin.save()
            course = cart.course
            datahistory = DataHistory.objects.create(
                buyer=request.user,
                course = course
            )
            course.sale_counter = course.sale_counter + 1
            course.save()
            datahistory.save()
            pdf_urls.append(cart.course.course_file.url)
            cart.delete()
        context={
            'pdf_urls':pdf_urls
        }
        return render(request, 'conformationpage.html',context)
    
@login_required(login_url='login/')
def history(request):
    historiesforbuy = DataHistory.objects.filter(buyer=request.user)
    historiesforsale = DataHistory.objects.filter(course_id=request.user.id)
    context = {
        'historiesforsale':historiesforsale,
        'historiesforbuy':historiesforbuy,
               }
    return render(request, "customerhistory.html" , context)


def becamesaller(request):
    user = CustomUser.objects.get(id=request.user.id)
    user.is_saller=True
    user.save()
    messages.info(request, "You are now a Saller..")
    return redirect("addcourse")
    