from django.shortcuts import render
from django.urls import resolve
from customer.models import Course, CustomUser

def home(request):
    courses = Course.objects.all()
    max_sale = 0
    for course in courses:
        if max_sale<course.sale_counter:
            max_sale=course.sale_counter
            
    hotcourse = Course.objects.get(sale_counter=max_sale)
    
    
    context={
        'hotcourse':hotcourse,
        "home":True
    }         
    print(hotcourse)
    return render(request, 'index.html',context)

def buycourse(request):
    courses= Course.objects.all().order_by("-id")
    context={
        "buycourse":True,
        "courses":courses
    }
    return render(request, 'buycourse.html',context)


def aboutmorecourse(request, id):
    course = Course.objects.get(id=id)
    context={
        "course":course,
        "buycourse":True
        
    }
    return render(request, 'aboutmorecourse.html', context)

def publishercourses(request, id):    
    backurl = request.META.get('HTTP_REFERER')
    course = Course.objects.get(id=id)
    customer = CustomUser.objects.get(id=course.user_id)
    usercourses = Course.objects.filter(user_id =customer.id)
    context={
        'backurl':backurl,
        'course':course,
        'usercourses':usercourses,
        'buycourse':True
    }
    return render(request, 'customercourses.html', context)


def contact(request):
    context={
        'contact':True
    }
    return render(request, 'contactpage.html', context)