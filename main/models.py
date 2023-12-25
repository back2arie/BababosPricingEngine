from django.db import models

class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Supplier(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=20)

class ProductSupplier(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    stock_available = models.IntegerField()

class RequestForQuotation(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    qty = models.IntegerField()

class PurchaseOrder(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    date = models.DateField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

class LogisticFleet(models.Model):
    type = models.CharField(max_length=100)
    capacity = models.IntegerField()

class LogisticCost(models.Model):
    fleet = models.ForeignKey("LogisticFleet", on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
