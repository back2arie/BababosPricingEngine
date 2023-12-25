from django.contrib import admin
from .models import ProductPrice
import locale

class ProductPriceAdmin(admin.ModelAdmin):
    locale.setlocale( locale.LC_ALL, 'IND' )
    list_display= ('id', 'product_id', 'product_name', 'cogs_price_currency', 'historical_price_currency', 'historical_price_margin_percentage', 'best_price_currency', 'best_price_margin_percentage', 'recommended_price_currency', 'recommended_price_margin_percentage')

    @admin.display(ordering='product__name', description='Product Name')
    def product_name(self, obj):
        return obj.product.name
    
    @admin.display(ordering='cogs_price', description='COGS Price')
    def cogs_price_currency (self, obj):
        return locale.currency( obj.cogs_price, grouping=True )
    
    @admin.display(ordering='historical_price', description='Historical Price')
    def historical_price_currency (self, obj):
        return locale.currency( obj.historical_price, grouping=True )
    
    @admin.display(ordering='historical_price_margin', description='Margin (%)')
    def historical_price_margin_percentage (self, obj):
        return obj.historical_price_margin

    @admin.display(ordering='best_price', description='Market\'s Best Price')
    def best_price_currency (self, obj):
        return locale.currency( obj.best_price, grouping=True )
    
    @admin.display(ordering='best_price_margin', description='Margin (%)')
    def best_price_margin_percentage (self, obj):
        return obj.best_price_margin
    
    @admin.display(ordering='recommended_price', description='Recommended Price')
    def recommended_price_currency (self, obj):
        return locale.currency( obj.recommended_price, grouping=True )

    @admin.display(ordering='recommended_price_margin', description='Margin (%)')
    def recommended_price_margin_percentage (self, obj):
        return obj.recommended_price_margin

admin.site.register(ProductPrice, ProductPriceAdmin)
