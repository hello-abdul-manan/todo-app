from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'completed', 'priority', 'due_date', 'created_at', 'updated_at')
    list_filter = ('completed', 'priority', 'user')
    search_fields = ('title',)
    ordering = ('-created_at',)
