from django.contrib import admin

from .models import Recipe, Ingredient, Tag


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug')
    list_filter = ('author', 'title', 'tags')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    list_filter = ('title', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'display_name')
    lsit_filter = ('title',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)