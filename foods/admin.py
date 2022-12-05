from django.contrib import admin
from foods.models import Food, FoodComment, FoodLike


admin.site.register(Food)
admin.site.register(FoodComment)
admin.site.register(FoodLike)