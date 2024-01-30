from django.urls import path

from .views import AllUsers

urlpatterns=[
    path("allusers/",AllUsers.as_view()),
]