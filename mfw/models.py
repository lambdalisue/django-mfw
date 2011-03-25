#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/23
#
from django.db import models
from django.utils.text import ugettext_lazy as _

class CIDRCache(models.Model):
    u"""CIDR cache database model"""
    carrier     = models.CharField(_('carrier'), max_length=30, unique=True)
    data        = models.TextField(_('data'))
    updated_at  = models.DateTimeField(_('updated at'), auto_now=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.carrier, self.updated_at)