#coding: utf-8
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription





def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_('CPF deve conter apenas números.'))

    if len(value) != 11: 
        raise ValidationError(_('CPF deve conter 11 números'))



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        
        self.fields['cpf'].validators.append(CPFValidator)
