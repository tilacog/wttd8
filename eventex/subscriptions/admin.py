#coding: utf-8
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, gettext as _
from django.contrib import admin
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at',
                     'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ['created_at']


    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True
    actions = ['mark_as_paid','invert_paid_status']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        msg = ungettext(
            u'%d inscrição foi marcada como paga.',
            u'%d inscrições foram marcadas como pagas.',
            count
        )
        self.message_user(request, msg % count)

    mark_as_paid.short_description = _('Marcar como pago')

    def invert_paid_status(self, request, queryset):
        'Inverts the payment status'
        count = 0
        for obj in queryset:
            if obj.paid == False:
                obj.paid=True
            elif obj.paid == True:
                obj.paid=False
            obj.save() 
            count += 1

        msg = ungettext(
            u'%d alteração de pagamento foi realizada',
            u'%d alterações de pagamento foram realizadas',
            count
        )

        self.message_user(request, msg % count)

    invert_paid_status.short_description = _('Inverter situação de pagamento')
admin.site.register(Subscription, SubscriptionAdmin)
