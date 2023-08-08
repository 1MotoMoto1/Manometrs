from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','price']
    prepopulated_fields = {'slug':('title',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','price','available','created', 'uploaded']
    list_filter = ['available','created','uploaded']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('title',)}
# Register your models here.
