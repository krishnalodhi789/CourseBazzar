from .models import CustomUser, AddToCart,CourseOffer
from django.contrib.auth.models import User

def profile_detail(request):
    user = request.user
    if user.username == "admin":
        customer = False
        return  {'customer':customer}
    
    if user.is_authenticated :
        customer = CustomUser.objects.get(id = user.id)
        cartcounter =  AddToCart.objects.filter(user_id = customer.id).count()
        carts =  AddToCart.objects.filter(user_id = customer.id)
        total_price = 0.00
        for cart in carts:
            if CourseOffer.objects.filter(course=cart.course).exists():
                total_price += CourseOffer.objects.get(course=cart.course).remaining_amount
            else:
                total_price += cart.course.price

        
        context={
            'customer':customer,
            'cartcounter' : cartcounter,
            'total_pay_price':total_price
        }       
    else:
        context={
            'customer':False
        }  
    return  context