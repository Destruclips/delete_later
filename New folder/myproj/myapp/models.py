from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date = models.DateField()
    InvoiceCustomerName = models.CharField(max_length=100)
    def __str__(self):
        return self.InvoiceCustomerName
class Invoice_Detail(models.Model):
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.Product