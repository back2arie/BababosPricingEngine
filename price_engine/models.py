from django.db import models

class ProductPrice(models.Model):
    product = models.ForeignKey("main.Product", on_delete=models.CASCADE)
    cogs_price = models.DecimalField(max_digits=12, decimal_places=4)
    historical_price = models.DecimalField(max_digits=12, decimal_places=4)
    historical_price_margin = models.DecimalField(max_digits=5, decimal_places=2)
    best_price = models.DecimalField(max_digits=12, decimal_places=4)
    best_price_margin = models.DecimalField(max_digits=5, decimal_places=2)
    recommended_price = models.DecimalField(max_digits=12, decimal_places=4)
    recommended_price_margin = models.DecimalField(max_digits=5, decimal_places=2)
