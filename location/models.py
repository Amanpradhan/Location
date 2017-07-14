# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Loc(models.Model):
	lat = models.DecimalField(max_digits=20, decimal_places=7)
	lon = models.DecimalField(max_digits=20, decimal_places=7)