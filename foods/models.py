from django.db import models
from users.models import User


# 카테고리 추가될 가능성 있음
class MainCategories(models.Model):
    main_category = models.CharField(max_length=20)

    def __str__(self):
        return self.main_category

class SubCategories(models.Model):
    sub_category = models.CharField(max_length=20)
    main_category = models.ForeignKey('MainCategories', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.sub_category


class Food(models.Model):
    food = models.CharField(max_length=30)
    food_img = models.ImageField(verbose_name="음식 사진", default="", upload_to="food")
    target = models.CharField(max_length=10, default="")
    main_category = models.ForeignKey(MainCategories, on_delete=models.CASCADE, default="")
    sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.food


class FoodComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="foodcomment_user")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="foodcomment_food")
    comment = models.TextField(verbose_name="음식 게시글 댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.food} / {self.comment}")