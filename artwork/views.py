# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, "artwork/products.html", {"products": products})

#We may need a paginator for this. Populate before testing
