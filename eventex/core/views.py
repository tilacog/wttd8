# coding: utf-8
'''
from django.shortcuts import render_to_response
from django.conf import settings


def homepage(request):
    context = {'STATIC_URL':settings.STATIC_URL}
    return render_to_response('index.html', context)
'''

from django.views.generic.simple import direct_to_template
    
def homepage(request):
    return direct_to_template(request, template="index.html")
