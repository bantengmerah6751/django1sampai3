from django.urls import path
from aplikasi_pertama import views

urlpatterns = [
    path('', views.index, name='index'),
]