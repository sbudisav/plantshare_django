from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'profiles'
urlpatterns = [
    path('home/<int:pk>', views.HomePageView.as_view(), name='home'),
    path('user/<str:username>', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
]