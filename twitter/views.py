from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views import generic
from .models import Hashtag, Tweet
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)   
            return redirect('home')
        except:
            return render(request, 'users/signup.html')
    return render(request, 'users/signup.html')


def splash(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'splash.html')


class Feed(LoginRequiredMixin, generic.ListView):
    template_name = 'home.html'
    login_url = 'splash'
    redirect_field_name = 'redirect_to'
    context_object_name = 'things'

    def get_queryset(self):
        tags_to_tweets = {}
        for tag in Hashtag.objects.all():
            if tag.content not in tags_to_tweets:
                tags_to_tweets[tag.content] = [tag.tweet]
            else:
                tags_to_tweets[tag.content].append(tag.tweet)

        queryset = {'tweets': Tweet.objects.order_by('-timestamp'), 'tag_tweet_map': tags_to_tweets}
        return queryset


def hashtag(request, tag_content):
    tagged_tweets = []
    if request.method == 'POST' and request.user.is_authenticated:  
        for tag in Hashtag.objects.all():
            if tag_content == tag.content:
                tagged_tweets.append(tag.tweet)
        return render(request, 'hashtag.html', {'hashtag': tag_content, 'tagged_tweets': tagged_tweets})
    return redirect('home')   


def create_tweet(request):
    if request.method == 'POST':
        content = request.POST["content"]
        user = request.user
        tweet = Tweet.objects.create(author=user, content=content)
        tags = []
        for word in content.split():
            if word.startswith('#') and len(word) > 1:
                word_set = word.split('#')
                for t in word_set:
                    if '#' not in t and len(t) >= 1:
                        tags.append(t)
        for tag in tags:
            Hashtag.objects.create(content=tag, tweet=tweet)
    return redirect('home')


def delete_tweet(request, id):
    if request.method == 'POST':
        tweet = Tweet.objects.get(id=id)
        tweet.delete()
    return redirect('home')


def like(request):
    user = request.user
    if request.method == 'POST' and user.is_authenticated:
        like_id = request.POST["like_id"]
        tweet = Tweet.objects.get(id=like_id)
        if tweet.likes.filter(id=user.id).exists():
            tweet.likes.remove(user)
        else:
            tweet.likes.add(user)
        print(request.path_info)
    return redirect('home')


def profile(request, id):
    if request.user.is_authenticated:  
        return render(request, 'users/profile.html', 
                        {'username': User.objects.get(id=id),
                        'profile_tweets': Tweet.objects.order_by('-timestamp').filter(author=id)})
    return redirect('home')

