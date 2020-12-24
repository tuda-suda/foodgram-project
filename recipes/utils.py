from django.db import transaction, IntegrityError
from django.http import HttpResponseBadRequest

from .models import Ingredient, RecipeIngredient



def get_ingredients_from_form(request):
    ingredients = {}
    for key in request.POST:
        var, num = key.split('_')
        if var == 'nameIngredient':
            ingredients[request.POST[key]] = request.POST[
                f'valueIngredient_{num}'
            ]
    
    return ingredients


def save_recipe(request, form):
    try:
        with transaction.atomic():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            objs = []
            ingredients = get_ingredients_from_form(request)
            for name, quantity in ingredients.items():
                ingredient = Ingredient.objects.get(name=name)
                objs.append(
                    RecipeIngredient(
                        recipe=recipe,
                        ingredient=ingredient,
                        quantity=quantity
                    )
                )
            RecipeIngredient.objects.bulk_create(objs)

            form.save_m2m()
            return recipe
    except IntegrityError:
        raise HttpResponseBadRequest
