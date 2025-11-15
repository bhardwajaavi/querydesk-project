# In tickets/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import QueryTicket, Profile
from django.contrib.auth.models import User

# This is your new "Unified Inbox"
@admin.register(QueryTicket)
class QueryTicketAdmin(admin.ModelAdmin):
    
    # --- 1. What you see in the main list ---
    list_display = (
        'subject', 
        'status', 
        'priority', 
        'category', 
        'submitted_by', 
        'assigned_to', 
        'created_at'
    )
    
    # --- 2. This is the "Routing" and "Tracking" feature ---
    # These fields can be edited DIRECTLY in the list
    list_editable = ('status', 'priority', 'assigned_to')
    
    # --- 3. This is the "Prioritization" filter ---
    list_filter = ('status', 'priority', 'category', 'assigned_to', 'created_at')
    
    # --- 4. This is the "Search" feature ---
    search_fields = ('subject', 'description', 'submitted_by__username')
    
    # --- 5. This is the "Resolution" feature ---
    # This organizes the "Edit" page for a single ticket
    
    # Make the user's original query "read-only"
    readonly_fields = ('subject', 'description', 'submitted_by', 'created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('subject', 'submitted_by', 'created_at')
        }),
        ('User Query Details', {
            'fields': ('description',)
        }),
        # This is YOUR section to "Triage" and "Resolve"
        ('Admin Triage & Resolution', {
            'fields': ('status', 'priority', 'category', 'assigned_to', 'admin_resolution')
        }),
    )

# --- This is the Profile-in-User-Admin code ---

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Unregister and reregister User
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)