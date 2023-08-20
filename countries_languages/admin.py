from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Person, Organization


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Персонал"""
    list_display = '__str__', 'birthday', 'organization', 'country', 'language', 'preview', 'created', 'updated'
    readonly_fields = 'preview',
    list_editable = 'country', 'language',

    def preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60" height="60" />')
        else:
            return 'Нет фотографии'

    preview.short_description = 'Фотография'


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Организация"""
    list_display = 'name',
