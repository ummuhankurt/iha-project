from django.shortcuts import render
from . models import Drone, Category

def iha_list(request):
    drones = Drone.objects.all()
    categories = Category.objects.all()
    context = {
        'drones' : drones,
        'categories' : categories
    }
    return render(request, 'iha-list.html',context)


def drones_by_category(request,category_slug):
    drones = Drone.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    context = {
        'drones' : drones,
        'categories' : categories
    }

    return render(request, 'iha-list.html',context)