from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display =  ('first_name', 'last_name', 'industry', 'locate', 'status', 'role')