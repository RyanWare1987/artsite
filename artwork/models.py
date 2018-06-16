# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings



class Product(models.Model):
    """
    The Product model will contain the path to where images
    are uploaded to in S3. Currently only the Admin can add these
    Products to the 'Store' Within this process we define the Product's
    Price, as well as Product details such as size, description, medium etc
    Views should default to 0, so we can track popularity of a product
    art_type should be 'MTG Alter', or 'Canvas' mainly. 
    In the future there could exist a filter on this.
    """
    image_width = 400
    image_height = 400

    product_images = models.ImageField(upload_to = 'media', 
                                        height_field='image_height',
                                        width_field='image_width',
                                        blank=True)
    name = models.CharField(max_length=180, default='')
    art_type = models.CharField(max_length=30, default='')
    medium = models.CharField(max_length=30, default='')
    size = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class OrderProduct(models.Model):
    """
    One form which the user is met with when heading to the 
    checkout. All fields are required and contain details of
    where to send the product and form part of the Stripe
    authentication check
    """

    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address_1 = models.CharField(max_length=40, blank=False)
    address_2 = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class PurchaseProduct(models.Model):
    """
    PurchaseProduct model links the product selected to the Order, 
    which is the model above.
    """
    order = models.ForeignKey(OrderProduct, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
