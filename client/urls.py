from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='client-home'),
    path('chat/',views.chat,name='client-chat'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('profile/timeline',views.profile_timeline,name='profile-timeline'),
    path('profile/about',views.profile_about,name='profile-about'),
    path('profile/connections',views.profile_connections,name='profile-connections'),
    path('profile/albums',views.profile_albums,name='profile-albums'),
]
app_name='client'