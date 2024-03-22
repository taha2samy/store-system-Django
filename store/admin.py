from django.contrib import admin
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('category', 'purchase_price', 'purchase_date', 'quantity', 'selling_price')
    list_filter = ('category', 'purchase_date')

