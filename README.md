# Twitter

## Juliana Lu

### How to Run
```
cd twitter192
pip install -r requirements.txt
python manage.py makemigrations twitter
python manage.py migrate
python manage.py runserver
```

### Routes
* ``` ``` - homepage with tweet feed and hashtag feed
* ```splash/``` - splash page with links to login and signup
* ```signup/``` - signup page
* ```accounts/login``` - login page
* ```profile/user=< id >``` - profile page for a given user
* ```hashtag/tag=< tag >``` - tweet feed for tweets with the given tag
