from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coming/', views.coming, name='coming')
    # path('whitepaper/', views.whitepaper, name='whitepaper')
]