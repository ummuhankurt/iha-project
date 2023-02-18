from django.shortcuts import render
def index(request):
    return render(request, "login.html") 

def login(request):
    return render(request, "login.html") 

def IhaListesi(request):
    return render(request, "iha-list.html")

def KayıtEkle(request):
    return render(request, "kayit-ekle.html")

def Register(request):
    return render(request, "register.html")