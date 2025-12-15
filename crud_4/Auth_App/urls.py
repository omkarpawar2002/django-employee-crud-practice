from django.urls import path
from .views import ( Sign_Up_View,Sign_In_View,Sign_Out_View )

urlpatterns = [
    path('sign_up/',Sign_Up_View,name='Sign_Up_View'),
    path('sign_in/',Sign_In_View,name='Sign_In_View'),
    path('sign_out/',Sign_Out_View,name='Sign_Out_View'),
]