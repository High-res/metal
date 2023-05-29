from django import forms
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_kz', 'is_published',)
    list_display_links = ('id', 'name', 'name_kz',)
    search_fields = ('name', 'name_kz', 'text', 'text_kz',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("name",)}

class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_kz', 'is_published',)
    list_display_links = ('id', 'name', 'name_kz',)
    search_fields = ('name', 'name_kz', 'text', 'text_kz',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("name",)}

class SubCategoryMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_kz', 'is_published',)
    list_display_links = ('id', 'name', 'name_kz',)
    search_fields = ('name', 'name_kz', 'text', 'text_kz',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("name",)}

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_kz', 'price', 'promotion_price', 'is_published',)
    list_display_links = ('id', 'name', 'name_kz',)
    search_fields = ('name', 'name_kz', 'text', 'text_kz',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {"slug": ("name",)}

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name',  'is_published',)
    list_display_links = ('id', 'company_name',)
    search_fields = ('company_name', 'company_title', 'company_title_kz',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'is_published',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)

admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(SubCategoryMenu, SubCategoryMenuAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Gallery, GalleryAdmin)