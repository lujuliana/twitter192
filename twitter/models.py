from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# class Profile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.DO_NOTHING
#     )
#     url = models.URLField(blank=True)

class Tweet(models.Model):
    class Meta:
        ordering = ["-timestamp"]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)

    # hashtags = models.ManyToManyField(Hashtag, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')

class Hashtag(models.Model):
    content = models.CharField(max_length=279)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, default='0')