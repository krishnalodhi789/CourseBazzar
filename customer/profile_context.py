from .models import CustomUser, AddToCart
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
            total_price += cart.course.price
        print(total_price)
        context={
            'customer':customer,
            'cartcounter' : cartcounter,
            'total_price':total_price
        }       
    else:
        context={
            'customer':False
        }  
    return  context