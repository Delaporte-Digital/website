from django.urls import path, include

from . import views


app_name = 'account'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<slug:username>/', views.user_page, name='user_page'),
]
