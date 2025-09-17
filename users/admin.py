from django.contrib import admin
from .models import User

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)