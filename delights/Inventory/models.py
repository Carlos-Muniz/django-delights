from django.db import models

# Create your models here.


class Ingredient(models.Model):
    POUND = "LB"
    TEASPOON = "TSP"
    TABLESPOON = "TBSP"
    CUP = "CUP"
    OUNCE = "OZ"
    PINT = "PINT"
    QUART = "QT"
    GALLON = "GAL"
    GRAM = "GRAM"
    COUNT = "CNT"

    UNIT_TYPE_CHOICES = [
        (TEASPOON, "Teaspoon"),
        (TABLESPOON, "Tablespoon"),
        (CUP, "Cup"),
        (OUNCE, "Ounce"),
        (PINT, "Pint"),
        (QUART, "Quart"),
        (GALLON, "Gallon"),
        (POUND, "Pound"),
        (GRAM, "Gram"),
        (COUNT, "Count"),
    ]
    name = models.CharField(max_length=64, primary_key=True)
    quantity = models.DecimalField(decimal_places=1, max_digits=4)
    unit = models.CharField(max_length=4, choices=UNIT_TYPE_CHOICES, default=POUND)


class MenuItem(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=1, max_digits=4)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)