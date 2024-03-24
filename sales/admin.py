from django.contrib import admin
from .models import *
import barcode
from io import BytesIO
from django.http import HttpResponse
from django.utils.safestring import mark_safe


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
    readonly_fields = ('item_pk',)
    fields = ('item_pk','item', 'quantity','Delivered', 'selling_price')
   # Set the primary key field as readonly
    
    def item_pk(self, instance):
        # Return the primary key of the item
        return instance.item.pk if instance.item else None
    item_pk.short_description = 'key'  # Customize the column header


class ReceiptAdmin(admin.ModelAdmin):
    inlines = [SellsInline]
    readonly_fields = ('total_price',)
    change_form_template = 'admin/Recept.html' 

admin.site.register(Receipt, ReceiptAdmin)
# Assuming your app is named 'your_app_name'
