from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #DELETE path('user-details/<int:pk>/', views.CustomUserDetails.as_view(), name='customuser_details'),
    #DELETE path('user-details/<username>/', views.CustomUserDetails.as_view(username=username), name='customuser_details'),
    path('user-details/<username>/', views.student_profile_view, name='student_profile')
]
