#coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):   
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = self.resp.context['form']
        self.assertItemsEqual(['name','email','cpf','phone'], form.fields)
    
    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)
    
    def test_email_is_optional(self):
        'Email is optional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)












    def make_validated_form(self, **kwargs):
        data = dict(name='Tiago',email='tiago@gmail.com',
                    cpf ='12345678901', phone='34414829')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

