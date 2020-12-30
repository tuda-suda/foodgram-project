from autoslug import AutoSlugField

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator


User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=150)
    dimension = models.CharField(max_length=10)


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
    )
    cooking_time = models.PositiveSmallIntegerField()
    slug = AutoSlugField(populate_from='title', allow_unicode=True)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amount'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Tag(models.Model):
    title = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
