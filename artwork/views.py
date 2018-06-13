# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import Product, PurchaseProduct
import stripe

stripe.api_key = settings.STRIPE_SECRET

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


@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            basket = request.session.get('basket', {})
            total = 0
            for id, quantity in basket.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                purchase_product = PurchaseProduct(
                    order = order, 
                    product = product,
                    quantity = quantity
                    )
                purchase_product.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['basket'] = {}
                return redirect(reverse('products'))
            else: 
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request, "We are unable to take payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
