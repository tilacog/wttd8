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
        data = dict(name='Tiago',email='tiago@gmail.com',
                    cpf ='12345678901', phone='34414829')
        data.update({'cpf':'ABCD5678901'})
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)
