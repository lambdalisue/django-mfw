#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from uamd import detect as _detect
from cidr import database_loader

def detect(meta):
    u"""Detect device via HTTP META info using `uamd` library"""
    device = _detect(meta, loader=database_loader)
    return device