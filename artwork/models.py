# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


#These will be the pieces of art on sale. From Canvas to AlterArt Cards
class Product(models.Model):

    image_width = 400
    image_height = 400

    product_images = models.ImageField(upload_to = 'media/products/%d/%m/%y',
                                        height_field='image_height',
                                        width_field='image_width',
                                        blank=True)
    name = models.CharField(max_length=180, default='')
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property #paypal form here
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name