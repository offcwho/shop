from django.contrib import admin

from store.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'price', 'image', 'is_active')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_active',)
    list_editable = ('category', 'price', 'is_active',)