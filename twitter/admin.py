from django.contrib import admin
from .models import Hashtag, Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'timestamp')

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content', 'tweet')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Hashtag, HashtagAdmin)