from .models import Customer
from django.contrib.auth.models import User

def profile_detail(request):
    user = request.user
    if user.username == "admin":
        customer = False
        return  {'customer':customer}
    
    if user.is_authenticated :
        customer = Customer.objects.get(user_id = user.id)        
    else:
        customer = False
    return  {'customer':customer}