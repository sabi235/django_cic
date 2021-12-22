from django.contrib import admin
from .models import Testapp


class TestappAdmin(admin.ModelAdmin):
    list_filter = ['name', 'slug']
    list_display = ['name', 'slug', 'description']
    list_editable = ['name']
    ordering = ['name', ]
    search_fields = ['name','slug']

admin.site.register(Testapp)