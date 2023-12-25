from django.contrib import admin
from .models import Customer, Supplier, Product, ProductSupplier, RequestForQuotation, PurchaseOrder, LogisticFleet, LogisticCost

class CustomerAdmin(admin.ModelAdmin):
    list_display= ('id', 'address', 'city', 'state')

class SupplierAdmin(admin.ModelAdmin):
    list_display= ('id', 'address', 'city', 'state')

class ProductAdmin(admin.ModelAdmin):
    list_display= ('id', 'code', 'name', 'unit_of_measure')

class ProductSupplierAdmin(admin.ModelAdmin):
    list_display= ('id', 'product_id', 'supplier_id', 'unit_price', 'stock_available')

class RequestForQuotationAdmin(admin.ModelAdmin):
    list_display= ('id', 'customer_id', 'product_id', 'product_name', 'qty', 'unit_of_measure')

    @admin.display(ordering='product__name', description='Product Name')
    def product_name(self, obj):
        return obj.product.name
    
    @admin.display(ordering='product__unit_of_measure', description='Unit of Measure')
    def unit_of_measure(self, obj):
        return obj.product.unit_of_measure

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display= ('id', 'customer_id', 'date', 'product_id', 'product_name', 'qty', 'unit_of_measure', 'unit_price')

    @admin.display(ordering='product__name', description='Product Name')
    def product_name(self, obj):
        return obj.product.name
    
    @admin.display(ordering='product__unit_of_measure', description='Unit of Measure')
    def unit_of_measure(self, obj):
        return obj.product.unit_of_measure

class LogisticFleetAdmin(admin.ModelAdmin):
    list_display= ('id', 'type', 'capacity')

class LogisticCostAdmin(admin.ModelAdmin):
    list_display= ('id', 'fleet_type', 'origin', 'destination', 'cost')

    @admin.display(ordering='logistic_fleet__type', description='Fleet Type')
    def fleet_type(self, obj):
        return obj.fleet.type

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSupplier, ProductSupplierAdmin)
admin.site.register(RequestForQuotation, RequestForQuotationAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(LogisticFleet, LogisticFleetAdmin)
admin.site.register(LogisticCost, LogisticCostAdmin)
