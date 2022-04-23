"""TransIndia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp import views as admin_views
from userapp import views as user_views
from mainapp import views as main_views
from captainapp import views as captain_views



urlpatterns = [

    # main path
    path('admin/', admin.site.urls),
    path('',main_views.home_index,name='home_index'),


    # admin path
    
    path('admin-signin',admin_views.admin_signin,name='admin_signin'),
    path('admin-signup',admin_views.admin_signup,name='admin_signup'),
    path('admin-bookings',admin_views.admin_view_bookings,name='admin_bookings'),
    path('admin-companies',admin_views.admin_view_companies,name='admin_companies'),
    path('admin-feedbacks',admin_views.admin_view_feedbacks,name='admin_feedbacks'),
    path('admin-users',admin_views.admin_view_users,name='admin_users'),
    path('admin-home',admin_views.admin_home,name='admin_home'),



# user path
    
    path('user-booking',user_views.user_booking,name='user_booking'),
    path('user-home',user_views.user_home,name='user_home'),
    path('user-login',user_views.user_login,name='user_login'),
    path('user-profile',user_views.user_profile,name='user_profile'),
    path('user-register',user_views.user_register,name='user_register'),



# captain path
    
    path('cap-login',captain_views.captain_login,name='cap_login'),
    path('cap-register',captain_views.captain_register,name='cap_register'),
    path('cap-payment',captain_views.captain_payment,name='cap_payment'),
    path('cap-order',captain_views.captain_order,name='cap_order'),
    path('cap-feedback',captain_views.captain_feedback,name='cap_feedback'),
    path('cap-profile',captain_views.captain_profile,name='cap_profile'),
    path('cap-home',captain_views.captain_home,name='cap_home'),
]

