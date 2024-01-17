from django.shortcuts import render
from django.urls import resolve
from customer.models import Course, CustomUser

def home(request):
    return render(request, 'index.html',{"home":True})

def buycourse(request):
    courses= Course.objects.all()
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
