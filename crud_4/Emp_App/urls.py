from django.urls import path
from .views import ( Add_Employee_View,Show_Employee_View,Update_Employee_View,Delete_Employee_View )

urlpatterns = [
    path('add_emp/',Add_Employee_View,name='Add_Employee_View'),
    path('show_emp/',Show_Employee_View,name='Show_Employee_View'),
    path('update_emp/<int:pk>/',Update_Employee_View,name='Update_Employee_View'),
    path('delete_emp/<int:pk>/',Delete_Employee_View,name='Delete_Employee_View')
]