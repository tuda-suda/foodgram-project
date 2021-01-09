from autoslug import AutoSlugField

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


class Ingredient(models.Model):
    """
    Stores a sigle Ingredient entry.
    """
    title = models.CharField(
        'Название ингредиента',
        max_length=150,
        db_index=True
    )
    dimension = models.CharField('Единица измерения', max_length=10)

    class Meta:
        ordering = ('title', )
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return f'{self.title}, {self.dimension}'


class Recipe(models.Model):
    """
    Stores a single Recipe entry. Related to `auth.User` , `recipes.Tag` and
    `recipes.Ingredient` through intermediate model `recipes.RecipeIngredient`.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    title = models.CharField('Название рецепта', max_length=200)
    image = models.ImageField('Изображение', upload_to='recipes/')
    text = models.TextField('Текст рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиент'
    )
    cooking_time = models.PositiveSmallIntegerField('Время приготовления')
    slug = AutoSlugField(populate_from='title', allow_unicode=True)
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Теги'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    """
    Intermediate model that supports a Many-to-Many relationship between
    `recipes.Recipe` and `recipes.Ingredient`.
    Also stores an additional `quantity` field.
    """
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Tag(models.Model):
    """
    Stores a single Tag entry.
    """
    title = models.CharField('Имя тега', max_length=50, db_index=True)
    display_name = models.CharField('Имя тега для шаблона', max_length=50)
    color = models.CharField('Цвет тега', max_length=50)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
