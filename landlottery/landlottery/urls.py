"""landlottery URL Configuration

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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('service', views.service, name='service'),
    path('show_service', views.show_service, name='show_service'),
    path('contact', views.contact, name="contact"),
    path('handle_contact', views.handle_contact, name="handle_contact"),
    path('all_flats', views.all_flats, name="all_flats"),
    path('location', views.location, name="location"),
    path('land-detail', views.detail, name="detail"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('error', views.error, name="error"),    
    path('logout', views.mylogout, name="logout"),
    path('handle_signup', views.handle_signup, name="handle_signup"),
    path('handle_login', views.handle_login, name="handle_login"),
    path('seller_change_pass', views.seller_change_pass, name="seller_change_pass"),
    path('seller_panel', views.seller_panel, name="seller_panel"),
    path('post_ad', views.post_ad, name="post_ad"),
    path('handle_post_ad', views.handle_post_ad, name="handle_post_ad"),
    path('my_ads', views.my_ads, name="my_ads"),
    path('delete_ads', views.delete_ads, name="delete_ads"),
    path('edit_ads', views.edit_ads, name="edit_ads"),
    path('handle_edit_ads', views.handle_edit_ads, name="handle_edit_ads"),
    path('handle_add_booking', views.handle_add_booking, name="handle_add_booking"),
    path('delete_booking', views.delete_booking, name="delete_booking"),
    path('user_panel', views.user_panel, name="user_panel"),
    path('user_login', views.user_login, name="user_login"),
    path('handle_user_login', views.handle_user_login, name="handle_user_login"),
    path('delete_booking_user', views.delete_booking_user, name="delete_booking_user"),
    path('edit_booking_user', views.edit_booking_user, name="edit_booking_user"),
    path('handle_edit_booking', views.handle_edit_booking, name="handle_edit_booking"),
    path('user_change_pass', views.user_change_pass, name="user_change_pass"),
    path('handle_change_pass', views.handle_change_pass, name="handle_change_pass"),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
