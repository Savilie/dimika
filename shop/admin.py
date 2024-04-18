from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}