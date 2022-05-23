from django.contrib import admin
from .models import category, product
# Register your models here.
admin.site.register(category)
admin.site.register(product)


"""
class CartOrderAdmin(admin.ModelAdmin):
    list_display=('user' ,'total_amt','paid_statue' ,'order_dt')
admin.site.register(CartOrder,CartOrderItemms)    



class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=('order' ,'invoice_no','item' ,'image','qty' ,'price','item' ,'total')
admin.site.register(CartOrderItemms,CartOrderItemsAdmin)


"""
