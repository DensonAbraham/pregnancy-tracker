from django.urls import path

from user_data.views import get_user, add_user, get_all_user



urlpatterns = [

    path("get_all_user", get_all_user, name="get_all_user"),

    path("get_user", get_user, name="get_user"),

    path("add_user", add_user, name="add_user"),


    # path("login", login, name="login")

]