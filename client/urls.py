from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='client-home'),
    path('chat/',views.chat,name='client-chat'),
]
app_name='client'