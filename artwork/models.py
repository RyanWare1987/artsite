# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


#These will be the pieces of art on sale. From Canvas to AlterArt Cards
class Product(models.Model):

    name = models.CharField(max_length=180, default='')
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property #paypal form here
