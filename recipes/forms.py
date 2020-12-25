from django import forms

from .models import Recipe, Tag


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'tags',
            'cooking_time',
            'description',
            'image',
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
