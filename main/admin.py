from django.contrib import admin
from models import *

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'descr')

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
