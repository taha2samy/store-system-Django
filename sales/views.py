from django.shortcuts import render
from django.http import JsonResponse,HttpResponseBadRequest
from store.models import *
from sales.models import *

import os

def get_receipt(request,id):
    try:
        get_id=Receipt.objects.get(id=id)
        elements=Sells.objects.filter(recept=get_id)
        total=0
        for e in elements:
            total += e.quantity*e.selling_price
            pass
        
        return render(request,'web/recept.html',{'elements':elements,'total':total,'id':id,'paid':get_id.Paid})
    except Receipt.DoesNotExist:
        return HttpResponseBadRequest('Invalid ID')
    except ValueError:
        return HttpResponseBadRequest('something in page')
    
    
    
def get_item_data(request,id):
    try:
        it = Store.objects.get(pk=int(id))
        item_data = {'id':it.id,
                     'quantity':it.quantity,
                     'selling_price':it.selling_price,
                     'category':it.category.pk,
                     'category_name':it.category.name}

        data = {'item': item_data}
        return JsonResponse(data)
    except Store.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)
    except ValueError:
        return HttpResponseBadRequest('Invalid ID')