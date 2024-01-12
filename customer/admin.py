from django.contrib import admin
from .models import Customer, Course ,AddToCart,Wallet, AmountTransitionHistory


admin.site.register(Customer)
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display =['customer','id','customer_id','approve','title',"course_file"]
    

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display =['customer','course']


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display =['user','balance']
    
@admin.register(AmountTransitionHistory)
class AmountTransitionHistoryAdmin(admin.ModelAdmin):
    list_display =['user','status',"amount"]