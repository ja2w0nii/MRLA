import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def collaborative_filtering(id):
    likes = pd.read_csv("foods/likes.csv")
    foods = pd.read_csv("foods/foods.csv", encoding="utf-8")

    pd.set_option("display.max_columns", 10)
    pd.set_option("display.width", 300)

    foods_likes = pd.merge(likes, foods, on="food_id")

    like_user = foods_likes.pivot_table("like", index=["user_id"], columns="food_id")
    like_user = like_user.fillna(0)

    user_based_collab = cosine_similarity(like_user, like_user)
    user_based_collab = pd.DataFrame(user_based_collab, index=like_user.index, columns=like_user.index)

    user = user_based_collab[id].sort_values(ascending=False)[:10].index[1]

    result = like_user.query(f"user_id == {user}").sort_values(ascending=False, by=user, axis=1)

    food_list = result.columns.values.tolist()

    return food_list
