from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("buy course/", buycourse, name="Buy Course"),
    path(
        "course/about more/<int:id>/",
        aboutmorecourse,
        name="About More Course",
    ),
    path(
        "course/about more/publishercourses/<int:id>/",
        publishercourses,
        name="Publisher Courses",
    ),
    
    path(
        "contact us/",
        contact,
        name="contact",
    ),
]
