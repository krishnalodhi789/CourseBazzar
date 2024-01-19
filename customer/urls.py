from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", signupform, name="signup"),
    path("login/", customerlogin, name="login"),
    path("logout/", customerlogout, name="customerlogout"),
    path(
        "deshboard/profile/",
        customerprofile,
        name="customerprofile",
    ),
    path("deshboard/addcourse/", addcourse, name="addcourse"),
    path(
        "deshboard/uploadedcourses/",
        uploadedcourses,
        name="uploadedcourses",
    ),
    path("add to cart/<int:id>/", addtocart, name="addtocart"),
    path("deshboard/carts/", customercart, name="customercart"),
    path(
        "deshboard/delete cart/<int:id>/", deletecart, name="deletecart"
    ), 
    path(
        "deshboard/wallet/", wallet, name="wallet"
    ),
    
    path(
        "deshboard/carts/conform order/", conformorder, name="conformorder"
    ),
    
    
    path(
        "deshboard/carts/conform order/comformation/", conformation, name="conformation"
    ),
    
    
    path(
        "deshboard/buying history/", buyinghistory, name="buyinghistory"
    ),
    
    path(
        "deshboard/selling history/", sellinghistory, name="sellinghistory"
    ),
    
    path(
        "became saller/", becamesaller, name="becamesaller"
    ),
]
