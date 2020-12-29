from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.db.models import Count

from .models import Recipe, Tag
from .forms import RecipeForm
from .utils import save_recipe, edit_recipe, compile_shop_list


User = get_user_model()


def index(request):
    tags = request.GET.getlist('tag', ['breakfast', 'lunch', 'dinner'])
    all_tags = Tag.objects.all()

    recipes = Recipe.objects.filter(
        tags__name__in=tags
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()

    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'recipes/indexAuth.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
        }
    )


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(
        Recipe.objects.select_related('author'),
        id=recipe_id
    )

    return render(request, 'recipes/singlePage.html', {'recipe': recipe})


@login_required
def recipe_new(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        recipe = save_recipe(request, form)
        print(recipe.tags)
        print(form.cleaned_data['tags'])

        return redirect('recipe_view', recipe_id=recipe.id)
    
    return render(request, 'recipes/formRecipe.html', {'form': form})


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
        print(recipe.tags)
        print(form.cleaned_data['tags'])
        edit_recipe(request, form, instance=recipe)
        return redirect('recipe_view', recipe_id=recipe.id)

    return render(
        request,
        'recipes/formRecipe.html',
        {'form': form, 'recipe': recipe}
    )


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
    return redirect('index')


def profile_view(request, username):
    author = get_object_or_404(User, username=username)
    author_recipes = author.recipes.all()

    paginator = Paginator(author_recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'recipes/authorRecipe.html',
        {
            'author': author,
            'page': page,
            'paginator': paginator
        }
    )


@login_required
def subscriptions(request):
    authors = User.objects.filter(
        following__user=request.user
    ).prefetch_related(
        'recipes'
    ).annotate(recipe_count=Count('recipes'))

    paginator = Paginator(authors, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'recipes/myFollow.html',
        {
            'page': page,
            'paginator': paginator,
        }
    )


@login_required
def favorites(request):
    tags = request.GET.getlist('tag', ['breakfast', 'lunch', 'dinner'])
    all_tags = Tag.objects.all()

    recipes = Recipe.objects.filter(
        favored_by__user=request.user,
        tags__name__in=tags
    ).select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).distinct()
    

    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request, 
        'recipes/favorite.html',
        {
            'page': page,
            'paginator': paginator,
            'tags': tags,
            'all_tags': all_tags,
        }
    )


@login_required
def purchases(request):
    recipes = request.user.shop_list.all()
    return render(
        request,
        'recipes/shopList.html',
        {'recipes': recipes},
    )


def purchases_download(request):
    recipes = request.user.shop_list.all()
    file = compile_shop_list(recipes)

    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename=ingredients.txt'
    return response
    