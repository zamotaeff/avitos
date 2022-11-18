from django.contrib import admin

from ads.models import Ad, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'is_published', 'category', 'id')
    list_display_links = ('name',)
    list_filter = ('is_published', 'category', 'author')
    list_editable = ('is_published', 'price')
    search_fields = ('name',)
