from django.urls import path


from . import views


app_name = 'hedge'

urlpatterns = [
    path('', views.hedge, name='hedge'),
]