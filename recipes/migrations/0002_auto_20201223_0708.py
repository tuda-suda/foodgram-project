# Generated by Django 3.1.4 on 2020-12-23 07:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='follow',
            name='author',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='noimage', upload_to='recipes/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=1, max_digits=6, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_amount', to='recipes.recipe'),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]