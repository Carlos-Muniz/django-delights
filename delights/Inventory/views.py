from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import logout

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "Inventory/home.html"


class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "Inventory/Ingredients.html"
    model = Ingredient


class CreateIngredientView(LoginRequiredMixin, CreateView):
    template_name = "Inventory/add_Ingredient.html"
    form_class = IngredientForm
    model = Ingredient


class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "Inventory/update_Ingredient.html"
    form_class = IngredientForm
    model = Ingredient


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    template_name = "Inventory/delete_Ingredient.html"
    model = Ingredient
    success_url = "/Ingredients"


class MenuItemsView(LoginRequiredMixin, ListView):
    template_name = "Inventory/MenuItems.html"
    model = MenuItem


class CreateMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "Inventory/add_MenuItem.html"
    form_class = MenuItemForm
    model = MenuItem


class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    template_name = "Inventory/update_MenuItem.html"
    form_class = MenuItemForm
    model = MenuItem


class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    template_name = "Inventory/delete_MenuItem.html"
    model = MenuItem
    success_url = "/MenuItems"


class RecipeRequirementsView(LoginRequiredMixin, ListView):
    template_name = "Inventory/RecipeRequirements.html"
    model = RecipeRequirement


class CreateRecipeRequirementView(LoginRequiredMixin, CreateView):
    template_name = "Inventory/add_RecipeRequirement.html"
    form_class = RecipeRequirementForm
    model = RecipeRequirement


class UpdateRecipeRequirementView(LoginRequiredMixin, UpdateView):
    template_name = "Inventory/update_RecipeRequirement.html"
    form_class = RecipeRequirementForm
    model = RecipeRequirement


class DeleteRecipeRequirementView(LoginRequiredMixin, DeleteView):
    template_name = "Inventory/delete_RecipeRequirement.html"
    model = RecipeRequirement
    success_url = "/RecipeRequirements"


class PurchasesView(LoginRequiredMixin, ListView):
    template_name = "Inventory/Purchases.html"
    model = Purchase


class CreatePurchaseView(LoginRequiredMixin, CreateView):
    template_name = "Inventory/add_Purchase.html"
    form_class = PurchaseForm
    model = Purchase


class UpdatePurchaseView(LoginRequiredMixin, UpdateView):
    template_name = "Inventory/update_Purchase.html"
    form_class = PurchaseForm
    model = Purchase


class DeletePurchaseView(LoginRequiredMixin, DeleteView):
    template_name = "Inventory/delete_Purchase.html"
    model = Purchase
    success_url = "/Purchases"


class FinancesView(LoginRequiredMixin, TemplateView):
    template_name = "Inventory/Finances.html"

    def get_context_data(self, **kwargs):
        context = {
            "total_cost": round(sum([p.get_cost() for p in Purchase.objects.all()]), 2),
            "total_revenue": round(sum(
                [p.get_revenue() for p in Purchase.objects.all()]
            ), 2),
            "total_profit": round(sum(
                [p.get_profit() for p in Purchase.objects.all()]
            ), 2)
        }
        return context


def log_out(request):
    logout(request)
    return redirect("/")

