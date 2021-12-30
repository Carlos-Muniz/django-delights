from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("Ingredients/", views.IngredientsView.as_view(), name="Ingredients"),
    path(
        "Ingredients/new/",
        views.CreateIngredientView.as_view(),
        name="create_Ingredient",
    ),
    path(
        "Ingredients/<pk>/update/",
        views.UpdateIngredientView.as_view(),
        name="update_Ingredient",
    ),
    path(
        "Ingredients/<pk>/delete/",
        views.DeleteIngredientView.as_view(),
        name="delete_Ingredient",
    ),
    path("MenuItems/", views.MenuItemsView.as_view(), name="MenuItems"),
    path("MenuItems/new/", views.CreateMenuItemView.as_view(), name="create_MenuItem"),
    path(
        "MenuItems/<pk>/update/",
        views.UpdateMenuItemView.as_view(),
        name="update_MenuItem",
    ),
    path(
        "MenuItems/<pk>/delete/",
        views.DeleteMenuItemView.as_view(),
        name="delete_MenuItem",
    ),
    path(
        "RecipeRequirements/",
        views.RecipeRequirementsView.as_view(),
        name="RecipeRequirements",
    ),
    path(
        "RecipeRequirements/new/",
        views.CreateRecipeRequirementView.as_view(),
        name="create_RecipeRequirement",
    ),
    path(
        "RecipeRequirements/<pk>/update/",
        views.UpdateRecipeRequirementView.as_view(),
        name="update_RecipeRequirement",
    ),
    path(
        "RecipeRequirements/<pk>/delete/",
        views.DeleteRecipeRequirementView.as_view(),
        name="delete_RecipeRequirement",
    ),
    path("Purchases/", views.PurchasesView.as_view(), name="Purchases"),
    path("Purchases/new/", views.CreatePurchaseView.as_view(), name="create_Purchase"),
    path(
        "Purchases/<pk>/update/",
        views.UpdatePurchaseView.as_view(),
        name="update_Purchase",
    ),
    path(
        "Purchases/<pk>/delete/",
        views.DeletePurchaseView.as_view(),
        name="delete_Purchase",
    ),
    path("Finances/", views.FinancesView.as_view(), name="Finances"),
]
