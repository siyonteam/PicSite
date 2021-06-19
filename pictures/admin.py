from django.contrib import admin
from .models import Picture,Category

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title' , 'user' , 'category' , 'tags' , 'updated')
    list_filter = ('user' , 'category' , 'tags' , 'updated')
    prepopulated_fields = {'slug':('title',)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'updated')
    list_filter = ('updated' ,)
    prepopulated_fields = {'slug':('name',)}