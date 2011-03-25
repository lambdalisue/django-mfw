#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from django.db import models
from django.utils.text import ugettext_lazy as _

class Comment(models.Model):
    device      = models.CharField(_('device name'), max_length=100, blank=True)
    comment     = models.CharField(_('comment'), max_length=100)
    created_at  = models.DateTimeField(_('created at'), auto_now_add=True)