from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('asibungalov/', views.home, name='asibungalov'),
  path('dogabungalov/', views.home, name='dogabungalov'),
  path('yildizbungalov/', views.home, name='yildizbungalov'),
]