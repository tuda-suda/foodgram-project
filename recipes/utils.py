from decimal import Decimal

from django.db import transaction, IntegrityError
from django.db.models import Sum
from django.http import HttpResponseBadRequest

from .models import Ingredient, RecipeIngredient



def get_ingredients(request):
    """
    Parse POST request body for ingredient names and their respective amounts.
    """
    ingredients = {}
    for key, name in request.POST.items():
        if key.startswith('nameIngredient'):
            num = key.split('_')[1]
            ingredients[name] = request.POST[
                f'valueIngredient_{num}'
            ]
    
    return ingredients


def save_recipe(request, form):
    """
    Create and save a Recipe instance with neccessary m2m relationships.
    """
    try:
        with transaction.atomic():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            objs = []
            ingredients = get_ingredients(request)
            for name, quantity in ingredients.items():
                ingredient = Ingredient.objects.get(title=name)
                objs.append(
                    RecipeIngredient(
                        recipe=recipe,
                        ingredient=ingredient,
                        quantity=Decimal(quantity.replace(',', '.'))
                    )
                )
            RecipeIngredient.objects.bulk_create(objs)

            form.save_m2m()
            return recipe
    except IntegrityError:
        raise HttpResponseBadRequest


def edit_recipe(request, form, instance):
    """
    A wrapper function for save_recipe to allow editing.
    """
    try:
        with transaction.atomic():
            RecipeIngredient.objects.filter(recipe=instance).delete()
            return save_recipe(request, form)
    except IntegrityError:
        raise HttpResponseBadRequest

    
def compile_shop_list(queryset):
    """
    Compile QuerySet of Purchase instances into list of individual ingredients.

    Each ingredient is represented using following format:
    • <ingredient title> (<dimension>) — <amount>
    """
    ingredients = queryset.select_related(
            'recipe'
        ).order_by(
            'recipe__ingredients__title'
        ).values(
            'recipe__ingredients__title', 'recipe__ingredients__dimension'
        ).annotate(amount=Sum('recipe__ingredients_amount__quantity')
    )

    return [
        (
            f"\u2022 {item['recipe__ingredients__title'].capitalize()} "
            f"({item['recipe__ingredients__dimension']}) "
            f"\u2014 {item['amount']}\n"
        ) for item in ingredients
    ]