#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

from forms import CommentForm
from models import Comment

import e4u
e4u.load()

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.device = unicode(request.device) or u""
            instance.save()
    else:
        form = CommentForm()
    kwargs = {
        'object_list': Comment.objects.order_by("-created_at")[:5],
        'form': form,
        'emoji_symbols': e4u._loader.symbols,
    }
    context = RequestContext(request, kwargs)
    return render_to_response(r"index.html", context_instance=context)