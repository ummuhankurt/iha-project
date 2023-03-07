from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('login/', views.login, name="login"),
    path('KayitEkle/', views.KayıtEkle, name="kayit-ekle"),
    path('register/', views.Register, name="register")
] 