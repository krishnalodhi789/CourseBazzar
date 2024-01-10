from .models import Customer, AddToCart
from django.contrib.auth.models import User

def profile_detail(request):
    user = request.user
    if user.username == "admin":
        customer = False
        return  {'customer':customer}
    
    if user.is_authenticated :
        customer = Customer.objects.get(user_id = user.id)
        print(customer.id)
        print(customer.user_id)
        print(user.id)
        cartcounter =  AddToCart.objects.filter(customer_id = customer.id).count()
        context={
            'customer':customer,
            'cartcounter' : cartcounter
        }       
    else:
        context={
            'customer':False
        }  
    return  context