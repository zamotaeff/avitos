from django.contrib import admin

from users.models import Location, User


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name', )
    search_fields = ('name', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'role', 'age', 'id')
    list_display_links = ('username', )
    list_filter = ('role', )
    list_editable = ('role', 'age')
    search_fields = ('first_name', 'last_name', 'username')
