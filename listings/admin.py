# listings/admin.py

from django.contrib import admin
from .models import HomeListing, TenantListing, SavedSearch

# Customizing the admin interface for HomeListing
@admin.register(HomeListing)
class HomeListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'municipality', 'rent_amount', 'is_wheelchair_friendly')
    search_fields = ('title', 'municipality')
    list_filter = ('is_wheelchair_friendly',)

# Customizing the admin interface for TenantListing
@admin.register(TenantListing)
class TenantListingAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Customizing the admin interface for SavedSearch
@admin.register(SavedSearch)
class SavedSearchAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality', 'rent_amount', 'is_wheelchair_friendly', 'user')
    search_fields = ('name', 'municipality')
    list_filter = ('is_wheelchair_friendly',)