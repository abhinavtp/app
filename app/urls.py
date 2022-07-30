from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='ho'),
    path('blog',views.blog,name='bl'),
    path('login',views.login,name='lo'),
    path('aboutus',views.aboutus,name='ab'),
    path('placement',views.placement,name='pl'),
    path('anwer',views.anwer,name='an')

]
