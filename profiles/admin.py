from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'role')  
    search_fields = ('user__username', 'location', 'role') 
