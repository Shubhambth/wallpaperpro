
from os import name
from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index,name="home"),
    path('upload/',views.upload_wallpaper,name='upload'),
    path('mupload/',views.mobile_wallpaper,name='mupload')
    
    
]
