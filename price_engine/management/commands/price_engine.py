from django.core.management.base import BaseCommand
from django.db.models import Min, Max
from main.models import Product, ProductSupplier, PurchaseOrder
from price_engine.models import ProductPrice
import random
import decimal

class Command(BaseCommand):
    help = "Price Engine"

    # COGS Price: based on supplier price lists and reverse bids
    # Historical Price: based on past sales (purchase orders)
    # Best Price: based on competitor prices
    # Recommended Price: based on the best price and the target margin

    def handle(self, *args, **kwargs):

        margin = decimal.Decimal(0.1) # 10% margin
        products = Product.objects.all()

        for product in products:

            cogs_price = ProductSupplier.objects.filter(product_id=product.id).aggregate(Min('unit_price'))['unit_price__min']
            historical_price = PurchaseOrder.objects.filter(product_id=product.id).aggregate(Max('unit_price'))['unit_price__max']
            historical_price_margin = self.calculate_margin(cogs_price, historical_price)
            best_price = historical_price + (historical_price * random.randrange(-50, 50)/100)
            best_price_margin = self.calculate_margin(cogs_price, best_price)

            recommended_price = 0
            
            # COGS Price is lower than best price
            # Doesn't make sense to sell below COGS Price
            # So, recommended price is COGS Price + margin
            if cogs_price > best_price:
                recommended_price = cogs_price + (cogs_price * margin)
            
            # Historical Price is higher than best price
            # Probably competition in certain product is low
            # So, recommended price is Best Price + margin to maximize profit
            elif historical_price > best_price:
                recommended_price = best_price + (best_price * margin)
            
            # Historical Price is lower than best price
            # Probably competition in certain product is high
            # So, recommended price is Best Price - margin to compete with competitors
            elif best_price > historical_price:
                recommended_price = best_price - (best_price * margin)

            recommended_price_margin = self.calculate_margin(cogs_price, recommended_price)

            if ProductPrice.objects.filter(product_id=product.id).exists():
                product_price = ProductPrice.objects.get(product_id=product.id)
                product_price.cogs_price = cogs_price
                product_price.historical_price = historical_price
                product_price.historical_price_margin = historical_price_margin
                product_price.best_price = best_price
                product_price.best_price_margin = best_price_margin
                product_price.recommended_price = recommended_price
                product_price.recommended_price_margin = recommended_price_margin
                product_price.save()
            else:
                product_price = ProductPrice.objects.create(
                    cogs_price=cogs_price,
                    historical_price=historical_price,
                    historical_price_margin=historical_price_margin,
                    best_price=best_price,
                    best_price_margin=best_price_margin,
                    recommended_price=recommended_price,
                    recommended_price_margin=recommended_price_margin,
                    product_id=product.id
                )
                
    def calculate_margin(self, cogs, price):
        percentage = ((price - cogs) / cogs) * 100
        return round(percentage, 2)