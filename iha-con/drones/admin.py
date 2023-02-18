from django.contrib import admin
from . models import Drone,Category



@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('brand','avaliable')
    list_filter = ('avaliable',)
    search_fields = ('brand','model')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('categoryName',)}