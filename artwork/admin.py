# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, OrderProduct, PurchaseProduct

#class OrderProductAdminInline(admin.TabularInline):
    #model = OrderProduct
    
#class OrderAdmin(admin.ModelAdmin):
    #inlines = (OrderProductAdminInline, )

admin.site.register(Product)

#admin.site.register(OrderProduct, OrderAdmin)