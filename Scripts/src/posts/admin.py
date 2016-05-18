from django.contrib import admin
from .models import post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","update","timestamp"]
    search_fields = ["title","content"]
    list_filter = ['update','timestamp']
    list_editable = ['title']
    list_display_links = ['update']


admin.site.register(post,PostModelAdmin)
