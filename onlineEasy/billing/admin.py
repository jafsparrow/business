from django.contrib import admin

from billing.models import Invoice
# Register your models here.

class IvoiceAdmin(admin.ModelAdmin):
    list_display = ('retail_order', 'invoice_date', 'payment')

admin.site.register(Invoice, IvoiceAdmin)
