from django.contrib import admin
from foods.models import Food, FoodComment, FoodLike, MajorCategory


admin.site.register(Food)
admin.site.register(FoodComment)
admin.site.register(FoodLike)
admin.site.register(MajorCategory)
# admin.site.register(MajorCategories)
# admin.site.register(MiddleCategories)
# admin.site.register(MinorCategories)
