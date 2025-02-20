from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/user_vote/", views.user_vote, name="user_vote"),
    path("register/", views.register, name="register"),
]