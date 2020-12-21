from autoslug import AutoSlugField

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField


User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    measure_unit = models.CharField(max_length=10)


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
    )
    tag = ArrayField(models.CharField(max_length=7), size=3)
    cooking_time = models.PositiveSmallIntegerField()
    slug = AutoSlugField(populate_from='name', allow_unicode=True)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        unique_together = ('user', 'author')
