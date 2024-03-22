from django.contrib import admin
from .models import *


@admin.register(Sells)
class SellsAdmin(admin.ModelAdmin):
    list_display = ('item', 'purchase_price', 'selling_date', 'quantity', 'selling_price')
    fields= ('item', 'quantity', 'selling_price','recept')
    list_filter = ('item', 'selling_date')
    search_fields = ('item__category',) 

    # Assuming Store has a 'name' field
class SellsInline(admin.TabularInline):
    model = Sells
    extra = 1  # Number of empty forms to display
    fields = ('item', 'quantity', 'selling_price')    
    def item_pk(self, instance):
        return instance.item.pk if instance.item else None
class ReceiptAdmin(admin.ModelAdmin):
    inlines = [SellsInline]
admin.site.register(Receipt, ReceiptAdmin)
# Assuming your app is named 'your_app_name'
