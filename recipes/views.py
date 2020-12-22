from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse

from .models import Recipe, Follow
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


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user.is_authenticated:
        template_name = 'singlePage.html'
    else:
        template_name = 'singlePageNotAuth.html'

    return render(request, template_name, {'recipe': recipe})


@login_required
def recipe_new(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        return redirect('recipe_view', recipe_id=recipe.id)
    
    return render(request, 'formRecipe.html', {'form': form})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe.id)

    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )
    if form.is_valid():
        form.save()
        return redirect('recipe_view', recipe_id=recipe.id)

    return render(request, 'formRecipe.html', {'form': form})


def profile_view(request, username):
    author = get_object_or_404(User, username=username)
    author_recipes = author.recipes.all()

    paginator = Paginator(author_recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        {
            'author': author,
            'page': page,
            'paginator': paginator
        }
    )
