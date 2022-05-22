from django.urls import path
from . import views

urlpatterns = [
     path('', views.adminhome, name='adminhome'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('users/<str:value>', views.admindelete, name='admindelete'),
    path('adminadd',views.adminadd, name='adminadd'),
    path('update/<int:id>', views.adminupdate, name='adminupdate'), 

]
