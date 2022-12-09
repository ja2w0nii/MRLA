from django.urls import path
from foods import views



urlpatterns = [
    path("main/", views.FoodView.as_view(), name="food_view"),
    path("main/<int:food_id>/", views.FoodDetailView.as_view(), name="food_detail_view"),
    path("main/<int:food_id>/comment/", views.FoodCommentView.as_view(), name="food_comment_view"),
    path("main/<int:food_id>/comment/<int:comment_id>/", views.FoodCommentView.as_view(), name="food_comment_view"),
    path("main/<int:food_id>/like/", views.LikeView.as_view(), name="like_view"),
    path("main/filtering/", views.FilteringFoodView.as_view(), name="filtering_food_view"),

    path("main/myfood/", views.MyFoodLikeView.as_view(), name="my_food_like_view"),
]
