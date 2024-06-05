from django.urls import path
from apphospital import views

urlpatterns = [
    path('', views.ok, name='ok'), 
]