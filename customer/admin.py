from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course ,AddToCart,Wallet, AmountTransitionHistory, BuyHistory,SaleHistory, CustomUser,CourseOffer



class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_buyer',
        'is_saller', 'phone','gender','image'
        )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_buyer', 'is_saller', 'phone','gender','image')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields':  ('is_buyer', 'is_saller', 'phone','gender','image')
        })
    )
admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(BuyHistory)
@admin.register(BuyHistory)
class BuyHistoryAdmin(admin.ModelAdmin):
    list_display =['buyer','course_id']

@admin.register(SaleHistory)
class SaleHistoryeAdmin(admin.ModelAdmin):
    list_display =['seller','course_id']


  
@admin.register(CourseOffer)
class CourseAdmin(admin.ModelAdmin):
    list_display =['saller',"course","get_offer"]
    
    def get_offer(self,instance)->str:
        return f"{instance.offer}%"
  

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display =['user','id','user_id','approve','title',"course_file"]
    

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display =['user','course']


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display =['user','balance']
    
@admin.register(AmountTransitionHistory)
class AmountTransitionHistoryAdmin(admin.ModelAdmin):
    list_display =['user','status',"amount"]