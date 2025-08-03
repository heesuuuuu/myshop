from django.contrib import admin
from .models import Product, Category

# admin 페이지에서 카테고리 직접 추가 가능 
admin.site.register(Product)
admin.site.register(Category)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created_at')
