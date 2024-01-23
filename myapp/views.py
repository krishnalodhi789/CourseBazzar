from django.shortcuts import render
from django.urls import resolve
from customer.models import Course, CustomUser, CourseOffer

def home(request):
    courses = Course.objects.all()
    max_sale = 0
    for course in courses:
        if max_sale<course.sale_counter:
            max_sale=course.sale_counter
    hotcourse = Course.objects.get(sale_counter=max_sale)
    
    offers = CourseOffer.objects.all().order_by('-offer')[:6]
    bestoffer = 0
    for course in offers:
        if bestoffer<course.offer:
            bestoffer=course.offer
    bestoffercourse = CourseOffer.objects.get(offer=bestoffer)
    offerprice = bestoffercourse.course.price-bestoffercourse.course.price/100*bestoffercourse.offer
    
    context={
        'hotcourse':hotcourse,
        'bestoffercourse':bestoffercourse,
        'offerprice':offerprice,
        'courses':offers,
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
    user = CustomUser.objects.get(id=course.user_id)
    usercourses = user.courses.all()
    print("=================================================")
    print(usercourses)
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