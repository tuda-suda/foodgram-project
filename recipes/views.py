from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from .models import Recipe, Ingredient, Follow, Favorites
from .forms import RecipeForm


User = get_user_model


def index(request):
    recipes = Recipe.objects.all().select_related('author')
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator
        }
    )


def recipe(request, id):
    recipe = get_object_or_404(Recipe.objects.select_related('ingredients'), id=id)
