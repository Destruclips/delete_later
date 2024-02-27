from django.contrib import admin

# Register your models here.
from .models import Invoice, Invoice_Detail
admin.site.register(Invoice)
admin.site.register(Invoice_Detail)