from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='feed-home'),
    path('chat/',views.chat,name='chat'),
    path('friends/',views.friends,name='friends'),

]
app_name='feed'