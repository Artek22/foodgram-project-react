from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import display


from .models import Ingredient, IngredientRecipe, Recipe, Tag
from users.models import User



@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',)
    list_filter = ('username', 'email')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags',)

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)


@admin.register(IngredientRecipe)
class IngredientRecipe(admin.ModelAdmin):
    list_display = ('recipe_id', 'ingredient_id', 'amount',)
