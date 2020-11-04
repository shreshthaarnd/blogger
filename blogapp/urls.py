from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
   
 path('admin/', admin.site.urls),
 path('index/',index),
 path('verify_user/',verify_user),
 path('archive/',archive),
 path('blog/',blog),
 path('category/',category),
 path('contact/',contact),
 path('element/',element),
 path('single_blog/',single_blog),
 path('usersave_trial/',usersave_trial),
 path('register/',register),
 path('login/',login),
 path('verify/',verify),
 path('postblog/',postblog),
]
