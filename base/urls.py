from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('asibungalov/', views.asibungalov, name='asibungalov'),
  path('dogabungalov/', views.dogabungalov, name='dogabungalov'),
  path('yildizbungalov/', views.yildizbungalov, name='yildizbungalov'),
]