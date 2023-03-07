from django.urls import path
from . import views
urlpatterns = [
    path('', views.iha_list,name="iha-list"),
    path('/<slug:category_slug>', views.drones_by_category,name="drones_by_category"),
] 