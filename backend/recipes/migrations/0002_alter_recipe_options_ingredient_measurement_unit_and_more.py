# Generated by Django 4.1.7 on 2023-03-27 13:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-id'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.CharField(default='г', max_length=128, verbose_name='Единица измерения'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(default='30', validators=[django.core.validators.MinValueValidator(1, message='Минимальное значение: 1')], verbose_name='Время приготовления'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipes/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='text',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default=1, max_length=7, validators=[django.core.validators.RegexValidator(message='Формат HEX-кода введен неправильно!', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='HEX-код'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=1, max_length=128, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=1, max_length=128, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient', verbose_name='Ингредиент')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list', to='recipes.recipe', verbose_name='Рецепт')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.IngredientRecipe', to='recipes.ingredient', verbose_name='Ингредиенты'),
        ),
    ]