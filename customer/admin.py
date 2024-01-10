from django.contrib import admin
from .models import Customer, Course ,AddToCart


admin.site.register(Customer)
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display =['customer','title',"course_file"]
    

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display =['customer','course']