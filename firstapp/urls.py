from django.conf.urls import url
from firstapp import views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    #path('user/', views.user, name='user'),
    path('userinfo/', views.userinput, name='userinfo'),
    path('result/', views.result, name='result'),
    path('recommendation/', views.after_result, name='after_result'),
    #path('myform/',views.myform, name='form')



]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)