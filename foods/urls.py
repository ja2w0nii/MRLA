from django.urls import path
from foods import views

urlpatterns = [
    path("main/", views.FoodView.as_view(), name="food_view"),
    path("main/<int:food_id>/", views.FoodDetailView.as_view(), name="food_detail_view"),
    path("main/<int:food_id>/comment/", views.FoodCommentView.as_view(), name="food_comment_view"),
    path("main/<int:food_id>/comment/<int:comment_id>/", views.FoodCommentView.as_view(), name="food_comment_view"),
    path("main/<int:food_id>/like/", views.LikeView.as_view(), name="like_view"),
    path("main/filtering/<int:category_id>/", views.FilteringFoodView.as_view(), name="filtering_food_view"),
    path("main/profile/<int:user_id>/likefood/", views.LikeFoodListView.as_view(), name="like_food_list_view"),
    path('main/search/', views.FoodSearchView.as_view(), name='food_search_view'),
]
