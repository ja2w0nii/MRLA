from django.urls import path
from foods import views


urlpatterns = [
    path('', views.FoodList.as_view(), name="food_list"),
    # path('filtering/', views.FoodLikeView.as_view(), name="food_like_view"),
    path('filtering/<int:user_id>/', views.FilteringFoodView.as_view(), name="filtering_food_view"),
]