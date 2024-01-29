from django.urls import path
from .views import index, loginform ,approved_course_list, not_approved_course_list
urlpatterns = [
	path('',index, name='superadmin_index'),
	path('login/',loginform, name='superadmin_loginform'),
	path('Approved Course List/',approved_course_list, name='superadmin_approved_course_list'),
	path('Not Approved Course List/',not_approved_course_list, name='superadmin_not_approved_course_list'),

]
