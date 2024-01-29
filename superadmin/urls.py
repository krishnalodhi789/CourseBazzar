from django.urls import path
from .views import course_offers, course_selling_history,index, loginform ,approved_course_list, not_approved_course_list, approved
urlpatterns = [
	path('',index, name='superadmin_index'),
	path('login/',loginform, name='superadmin_loginform'),
	path('Approved Course List/',approved_course_list, name='superadmin_approved_course_list'),
	path('Not Approved Course List/',not_approved_course_list, name='superadmin_not_approved_course_list'),
	path('Approved/<int:id>/',approved, name='superadmin_approve'),
	path('Course Offers/',course_offers, name='superadmin_course_offers'),
	path('Course Selling History/',course_selling_history, name='superadmin_course_selling_history'),

]
