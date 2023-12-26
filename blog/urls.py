from django.urls import path


from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.list_view, name='list_view'),
]