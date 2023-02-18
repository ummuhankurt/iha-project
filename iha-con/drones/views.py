from django.shortcuts import render
from . models import Drone

def iha_list(request):
    drones = Drone.objects.all()
    context = {
        'drones' : drones
    }
    return render(request, 'iha-list.html',context)
