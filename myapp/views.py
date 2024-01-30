from django.shortcuts import render
from django.urls import resolve
from customer.models import Course, CustomUser, CourseOffer,CourseCategory

def home(request):
    courses = Course.objects.all()
    max_sale = 0
    for course in courses:
        if max_sale<course.sale_counter:
            max_sale=course.sale_counter
    hotcourse = Course.objects.filter(sale_counter=max_sale).first()
    
    offers = CourseOffer.objects.all().order_by('-offer')[:6]
    bestoffer = 0
    for course in offers:
        if bestoffer<course.offer:
            bestoffer=course.offer
    bestoffercourse = CourseOffer.objects.get(offer=bestoffer)
    
    bestsellerscourses = Course.objects.all().order_by('-sale_counter')[:6]

    categories = CourseCategory.objects.all()
    context={
        'hotcourse':hotcourse,
        'bestoffercourse':bestoffercourse,
        'courses':offers,
        'bestsellerscourses':bestsellerscourses,
        'categories':categories,
        "home":True
    }         
    print(hotcourse)
    return render(request, 'index.html',context)

def buycourse(request):
    category_name = request.GET.get("category")
    print(category_name)
    courses=[]     
    if category_name is not None:
        # if CourseCategory.objects.filter(category_name__icontains=category_name).exists():
        #     category = CourseCategory.objects.filter(category_name__icontains=category_name)
        #     print(category)
        #     courses= Course.objects.filter(category=category)
        category = CourseCategory.objects.filter(category_name__icontains=category_name)
        for i in category:
            print(i)
            data=Course.objects.filter(category=i)
            courses.extend(data)
        print(courses)
    else:
        courses= Course.objects.all().order_by("-id")

    selected_category =category_name
    categories = CourseCategory.objects.all()
    context={
        "buycourse":True,
        "courses":courses,
        "categories":categories,
        "selected_category":selected_category,
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


def super_deals(request):
    bestoffercourses = CourseOffer.objects.all().order_by("-offer")[:3]
    otheroffercourses = CourseOffer.objects.all().order_by("-offer")[3:]
    print(bestoffercourses)
    context={
        'bestoffercourses':bestoffercourses,
        "superdealspage":True,
        'otheroffercourses':otheroffercourses
    }
    return render(request, 'superdeals.html', context)


def aboutus(request):
    context={
    'aboutus':True
    }
    return render(request, 'aboutus.html',context)