#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/25
#
from django import forms
from models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )