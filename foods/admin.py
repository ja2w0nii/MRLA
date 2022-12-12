from django.contrib import admin
from foods.models import Food, FoodComment, FoodLike, MainCategories, SubCategories




admin.site.register(Food)
admin.site.register(FoodComment)
admin.site.register(FoodLike)
admin.site.register(MainCategories)
admin.site.register(SubCategories)

