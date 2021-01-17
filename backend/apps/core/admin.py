from django.contrib import admin
from .models import List, Item


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


admin.site.register(List, ListAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'list')


admin.site.register(Item, ItemAdmin)