from django.urls import path, re_path
from . import views

urlpatterns = [
 path('', views.Feed.as_view(), name = "home"),
 path('signup/', views.signup, name='signup'),
 path('splash/', views.splash, name='splash'),
 path('create_tweet/', views.create_tweet, name="create tweet"),
 path('delete_tweet/id=<id>', views.delete_tweet, name="delete_tweet"),
 re_path('like/', views.like, name="like"),
 path('hashtag/tag=<tag_content>', views.hashtag, name="hashtag"),
 path('profile/user=<id>', views.profile, name="profile")
]