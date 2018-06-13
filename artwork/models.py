# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings


#These will be the pieces of art on sale. From Canvas to AlterArt Cards
class Product(models.Model):

    image_width = 400
    image_height = 400

    product_images = models.ImageField(upload_to = 'media',   #Current local path does not work, try when up to S3
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
    # A model to handle the details for purchasing a product

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
    # Model which contains Ordering Details, along with Product information

    order = models.ForeignKey(OrderProduct, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
