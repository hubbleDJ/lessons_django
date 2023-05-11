# Register your models here.

from django.contrib import admin
from products.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    search_fields = ('name', 'description')
    ordering = ('name', ) # если в обратном порядке то -name


class BusketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0