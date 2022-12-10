from django.db import models
from users.models import User



class Food(models.Model):
    class Meta:
        db_table = "food"

    food_id = models.IntegerField(primary_key=True, unique=True)
    menu = models.CharField(verbose_name="음식명", max_length=50)
    image = models.ImageField(verbose_name="음식 사진", blank=True)
    major_category = models.CharField(verbose_name="대분류", max_length=50)
    middle_category = models.CharField(verbose_name="중분류", max_length=50)
    minor_category = models.CharField(verbose_name="소분류", max_length=50)
    target = models.CharField(verbose_name="같이 먹는 대상", max_length=50)

    likes = models.ManyToManyField(User, verbose_name="좋아요 음식", through="FoodLike", related_name="food_likes", blank=True)

    def __str__(self):
        return str(self.menu)


class FoodLike(models.Model):
    class Meta:
        db_table = "food_like"

    user = models.ForeignKey(User, verbose_name="좋아요 등록 유저", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, verbose_name="음식명", on_delete=models.CASCADE)
    like = models.IntegerField(verbose_name="좋아요", default=True)

    def __str__(self):
        return str(f'{self.food} / {self.like}')


class FoodComment(models.Model):
    class Meta:
        db_table = "food_comment"

    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="foodcomment_user")
    menu = models.ForeignKey(Food, verbose_name="음식명", on_delete=models.CASCADE, related_name="foodcomment_menu")
    comment = models.TextField(verbose_name="음식 댓글", max_length=500)
    created_at = models.DateTimeField(verbose_name="작성 시간", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정 시간", auto_now=True)

    def __str__(self):
        return str(f"{self.user} / {self.menu} / {self.comment}")

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



