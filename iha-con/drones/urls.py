from django.urls import path
from . import views
urlpatterns = [
    path('', views.iha_list,name="iha-list"),
] 