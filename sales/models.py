from django.db import models
from store.models import *
class Sells(models.Model):
    item=models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    recept=models.ForeignKey('Receipt', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.pk)   
@receiver(pre_save, sender=Sells)
def before_save_sells(sender, instance, **kwargs):
    if instance.pk is None:
        print(instance.quantity,instance.item.quantity)
        if instance.quantity <= instance.item.quantity:
            instance.item.quantity -=instance.quantity
            instance.item.save()
            
        else:
            # send message to user amount is not enough
            pass
    else:
        quantity_store=Sells.objects.filter(pk=instance.pk)
        var = quantity_store[0].quantity-instance.quantity
        if var==0:
            pass
        elif  var>0:
            instance.item.quantity +=var
            instance.item.save()
        elif var<0:
            if instance.item.quantity >= var:
                instance.item.quantity -=abs(var)
                instance.item.save()
            else:
                # message
                pass
    instance.purchase_price=instance.item.purchase_price

@receiver(pre_delete, sender=Sells)
def before_delete_sells(sender, instance, **kwargs):
    instance.item.quantity +=instance.quantity
    instance.item.save()

class Receipt(models.Model):
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return str(self.pk)