from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
 path('admin/', admin.site.urls),
 path('index/',index),
 path('archive/',archive),
 path('blog/',blog),
 path('category/',category),
 path('contact/',contact),
 path('element/',element),
 path('single_blog/',single_blog),
 path('register/',register),
 path('login/',login),
 path('verify/',verify),
 path('postblog/',postblog),
 path('usersave/',usersave),
 path('verify_user/',verify_user),
 path('checklogin/',checklogin),
 path('blogsave/',blogsave),
 path('logout/',logout),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)