# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

def productsall(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

#We may need a paginator for this. Populate before testing
