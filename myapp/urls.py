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
    path(
        "super deals/",
        super_deals,
        name="super_deals",
    ),

    path(
        "About Us/",
        aboutus,
        name="aboutus",
    ),
]
