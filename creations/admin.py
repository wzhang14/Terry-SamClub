from django.contrib import admin

from .models import Creation


class CreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'creator', 'create_date', 'category')
    list_display_links = ('id', 'title')
    list_filter = ('creator',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'category')
    list_per_page = 25


admin.site.register(Creation, CreationAdmin)
