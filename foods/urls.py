from django.urls import path
from foods import views

urlpatterns = [
    path("main/", views.FoodView.as_view(), name="food_view"),
    path("main/<int:food_id>/", views.FoodCommentView.as_view(), name="food_comment_view"),
    path("main/<int:food_id>/comment/<int:comment_id>/", views.FoodCommentView.as_view(), name="food_comment_view"),
]
