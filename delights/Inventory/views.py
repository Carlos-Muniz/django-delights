from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = "Inventory/home.html"


class IngredientsView(ListView):
    template_name = "Inventory/Ingredients.html"
    model = Ingredient


class CreateIngredientView(CreateView):
    template_name = "Inventory/add_Ingredient.html"
    form_class = IngredientForm
    model = Ingredient


class UpdateIngredientView(UpdateView):
    template_name = "Inventory/update_Ingredient.html"
    form_class = IngredientForm
    model = Ingredient


class DeleteIngredientView(DeleteView):
    template_name = "Inventory/delete_Ingredient.html"
    model = Ingredient
    success_url = "/Ingredients"


class MenuItemsView(ListView):
    template_name = "Inventory/MenuItems.html"
    model = MenuItem


class CreateMenuItemView(CreateView):
    template_name = "Inventory/add_MenuItem.html"
    form_class = MenuItemForm
    model = MenuItem


class UpdateMenuItemView(UpdateView):
    template_name = "Inventory/update_MenuItem.html"
    form_class = MenuItemForm
    model = MenuItem


class DeleteMenuItemView(DeleteView):
    template_name = "Inventory/delete_MenuItem.html"
    model = MenuItem
    success_url = "/MenuItems"


class RecipeRequirementsView(ListView):
    template_name = "Inventory/RecipeRequirements.html"
    model = RecipeRequirement


class CreateRecipeRequirementView(CreateView):
    template_name = "Inventory/add_RecipeRequirement.html"
    form_class = RecipeRequirementForm
    model = RecipeRequirement


class UpdateRecipeRequirementView(UpdateView):
    template_name = "Inventory/update_RecipeRequirement.html"
    form_class = RecipeRequirementForm
    model = RecipeRequirement


class DeleteRecipeRequirementView(DeleteView):
    template_name = "Inventory/delete_RecipeRequirement.html"
    model = RecipeRequirement
    success_url = "/RecipeRequirements"


class PurchasesView(ListView):
    template_name = "Inventory/Purchases.html"
    model = Purchase


class CreatePurchaseView(CreateView):
    template_name = "Inventory/add_Purchase.html"
    form_class = PurchaseForm
    model = Purchase


class UpdatePurchaseView(UpdateView):
    template_name = "Inventory/update_Purchase.html"
    form_class = PurchaseForm
    model = Purchase


class DeletePurchaseView(DeleteView):
    template_name = "Inventory/delete_Purchase.html"
    model = Purchase
    success_url = "/Purchases"


class FinancesView(TemplateView):
    template_name = "Inventory/Finances.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context