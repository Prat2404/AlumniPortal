from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='user-login'),
    path('signup/',views.signup,name='user-signup'),
    path('logout/',views.logout,name='user-logout')
]