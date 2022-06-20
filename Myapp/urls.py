from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path('',views.dashboard,name='Deshboard'),
    path('home/',views.home,name='Home'),
    path('video/',views.video,name='Video'),
    path('about/',views.about,name='About'),
    path('contact',views.contact,name='Contact'),
]