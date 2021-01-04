from django.contrib import admin
from django.db.models import Count

from .models import Recipe, Ingredient, Tag, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0
    verbose_name = 'ингредиент'


class TagInline(admin.TabularInline):
    model = Tag
    min_num = 1
    extra = 0
    verbose_name = 'тег'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, Tag)
    list_display = (
        'id', 'title', 'author', 'slug',
        'duration', 'tags', 'get_favorite_count'
    )
    list_filter = ('author', 'tags__title')
    search_fields = ('title', 'author__username')
    autocomplete_fields = ('author')
    ordering = ('-pub_date')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(favorite_count=Count('favored_by'))

    def get_favorite_count(self, obj):
        return obj.favorite_count


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'dimension')
    list_filter = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'display_name')
    list_filter = ('title',)
