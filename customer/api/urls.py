from django.urls import path

from .views import AllUsers, AllBuyers, AllSellers, UserDetail,CreateUser

urlpatterns=[
    path("all-users/",AllUsers.as_view()),
    path("all-buyers/",AllBuyers.as_view()),
    path("all-sellers/",AllSellers.as_view()),
    path("user-detail/<int:id>/",UserDetail.as_view()),
    path("create-user/",CreateUser.as_view()),
]