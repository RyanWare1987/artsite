# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Product

def productsall(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

#We may need a paginator for this. Populate before testing


def productdetail(request, id):
    product = Product.objects.all()
    product = get_object_or_404(Product, pk=id)
    product.views += 1 #This adds 1 to the number of views this item has had
    product.save()
    return render(request, "productdetail.html", {"product": product})