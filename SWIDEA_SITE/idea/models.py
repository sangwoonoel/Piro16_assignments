
from django.db import models




class Devtool(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Idea(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="poster", null=True, blank=True)

    #img
    content = models.CharField(max_length=100)
    interest = models.IntegerField(null=True, blank=True)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


