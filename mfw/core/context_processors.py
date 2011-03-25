#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
def device(request):
    return {'device': request.device}

def flavour(request):
    return {'flavour': request.flavour}