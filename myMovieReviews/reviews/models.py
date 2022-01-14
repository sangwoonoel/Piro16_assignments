from distutils.log import warn
from django.db import models

class Review(models.Model):
    ACTION = 'AC'
    SF = 'SF'
    COMEDY = 'CO'
    ROMEDY = 'RO'
    THRILLER = 'TH'
    HORROR = 'HO'
    WAR = 'WA'
    SPORTS = 'SP'
    MUSICAL = 'MU'
    MELODRAMA = 'ME'
    ANIMATION = 'AN'
    CRIME = ' CR'
    GENRE_IN_MOVIE_CHOICES = [
        (ACTION, 'Action'),
        (SF, 'SF'),
        (COMEDY, 'Comedy'),
        (ROMEDY, 'Romedy'),
        (THRILLER, 'Thriller'),
        (HORROR, 'Horror'),
        (WAR, 'War'),
        (SPORTS, 'Sports'),
        (MUSICAL, 'Musical'),
        (MELODRAMA, 'Melodrama'),
        (ANIMATION, 'Animation'),
        (CRIME, 'Crime'),
    ]
    title = models.CharField(verbose_name = '제목', max_length=100)
    year = models.CharField(verbose_name = '개봉 년도', max_length=50)
    genre = models.CharField(verbose_name = '장르', max_length=50, choices=GENRE_IN_MOVIE_CHOICES)
    star = models.FloatField(verbose_name = '별점', max_length=50)
    time = models.IntegerField(verbose_name = '러닝타임')
    content = models.TextField(verbose_name = '리뷰')
    director = models.CharField(verbose_name = '감독', max_length=50)
    actor = models.CharField(verbose_name = '배우', max_length=50)


    def __str__(self):
        return self.title