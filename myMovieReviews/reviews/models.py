from django.db import models

class Review(models.Model):
    title = models.CharField(verbose_name = '제목', max_length=100)
    year = models.CharField(verbose_name = '개봉 년도', max_length=50)
    genre = models.CharField(verbose_name = '장르', max_length=50)
    star = models.CharField(verbose_name = '별점', max_length=50)
    time = models.CharField(verbose_name = '러닝타임', max_length=50)
    content = models.TextField(verbose_name = '리뷰')
    director = models.CharField(verbose_name = '감독', max_length=50)
    actor = models.CharField(verbose_name = '배우', max_length=50)


    def __str__(self):
        return self.title