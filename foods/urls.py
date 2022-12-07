from django.urls import path
from foods import views


urlpatterns = [
    path('', views.FoodList.as_view(), name="food_list"),
    path('filtering/', views.FilteringFoodView.as_view(), name="filtering_food_view"),
    # path('filtering/', views.FoodLikeView.as_view(), name="food_like_view"),
    path('like/<int:food_id>/', views.LikeView.as_view(), name="like_view"),
]
