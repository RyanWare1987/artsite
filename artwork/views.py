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
    """
    This view will list all products
    which are currently stored within 
    the database
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})



def productdetail(request, id):
    """
    This view is responsible for taking the user
    to a page which shows more information about
    the selected product. We pass in the Product ID
    to determin what product data is called and 
    passed into productdetail.html
    - Product Views will add 1 to the count or views
    """
    product = Product.objects.all()
    product = get_object_or_404(Product, pk=id)
    product.views += 1 
    product.save()
    return render(request, "productdetail.html", {"product": product})



"""
We would only like logged in users to proceed
to the checkout. Any uers not logged in
will be propmted to login via the login page
"""
@login_required()
def checkout(request):
    """
    This view will combine both OrderForm & MakePaymentForm
    forms that are created in this application.
    """
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            """
            If the above two arguments are true, 
            we request the basket session to be called 
            upon, so that we can setup the process to 
            charge the customer
            """
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
                """
                Tested with the Stripe Test Details, and this 
                information is what we want to land in our Stripe 
                Account Inbox, in particular the email of the 
                registered user.
                """
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
