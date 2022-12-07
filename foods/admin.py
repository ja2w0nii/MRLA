from django.contrib import admin
from foods.models import Food, FoodComment, MainCategories, SubCategories


admin.site.register(Food)
admin.site.register(FoodComment)
admin.site.register(MainCategories)
admin.site.register(SubCategories)