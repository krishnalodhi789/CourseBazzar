from ..models import CustomUser, Course, CourseCategory, CourseHistory

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('id',"username",'password',"email","first_name","last_name","phone","gender","is_buyer","is_seller","image")




class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields=['category_name']

class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer()
    class Meta:
        model=Course
        fields = ['id','title','key_points','description','price','category','sale_counter','published_datetime','approval_datetime','approve','course_file','image']

class SellerSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(read_only=True, many=True)
    class Meta:
        model=CustomUser
        fields=['id',"username",'password',"email","first_name","last_name","phone","gender","image",'courses']






class CourseBuyingHistorySerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model=CourseHistory
        fields = ["course",'datetime']


class BuyerSerializer(serializers.ModelSerializer):
    buyhistories = CourseBuyingHistorySerializer(many=True)
    class Meta:
        model=CustomUser
        fields=['id',"username",'password',"email","first_name","last_name","phone","gender","image",'buyhistories']



class UserDetailSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(read_only=True, many=True)
    buyhistories = CourseBuyingHistorySerializer(many=True)
    class Meta:
        model=CustomUser
        fields=('id',"username",'password',"email","first_name","last_name","phone","gender","is_buyer","is_seller","image",'courses',"buyhistories")


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("username",'password',"email","first_name","last_name","phone","gender",)





