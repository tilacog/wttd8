#coding: utf-8

from django.views.generic.simple import direct_to_template


def subscribe(request):
    return direct_to_template(request, 'subscriptions/subscription_form.html')
