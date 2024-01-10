from django.shortcuts import render
from customer.models import Course

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

def customercourses(request, id):
    backurl = request.META.get('HTTP_REFERER')
    backcourse = Course.objects.get(id=id)
    customercourses = Course.objects.filter(customer_id =backcourse.id)
    print(customercourses)
    context={
        'backurl':backurl,
        'backcourse':backcourse,
        'customercourses':customercourses,
        'buycourse':True
    }
    return render(request, 'customercourses.html', context)
