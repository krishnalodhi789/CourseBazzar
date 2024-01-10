"""
URL configuration for coursebazzar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views as myapp_view
from customer import views as customer_view
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # myapp app URLs ---------------------------------------
    path("",myapp_view.home, name='home'),
    path("buy course/",myapp_view.buycourse, name='buycourse'),
    path("course/about more/<int:id>/",myapp_view.aboutmorecourse, name='aboutmorecourse'),
    path("course/about more/customer courses/<int:id>/",myapp_view.customercourses, name='customercourses'),
    
    
    # Customer app URLs -------------------------------------------
    path("signup/", customer_view.signupform, name='signup'),
    path("login/", customer_view.customerlogin, name='login'),
    path("logout/", customer_view.customerlogout, name='customerlogout'),
    path("customer/deshboard/profile/", customer_view.customerprofile, name='customerprofile'),
    path("customer/deshboard/addcourse/", customer_view.addcourse, name='addcourse'),
    path("customer/deshboard/uploadedcourses/", customer_view.uploadedcourses, name='uploadedcourses'),
    path("customer/add to cart/<int:id>/", customer_view.addtocart, name='addtocart'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)