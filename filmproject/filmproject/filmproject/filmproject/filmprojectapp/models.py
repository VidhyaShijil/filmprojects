from django.db import models

# Create your models here.
class Addmovie(models.Model):
    
    name=models.CharField(max_length=250)
    desc=models.TextField()
    actor=models.TextField()
    date=models.TextField()
    link=models.TextField()
    category=models.TextField()
    year=models.IntegerField()
    userid=models.IntegerField()
    img=models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.name
    
class Review(models.Model):
    description = models.TextField()
    stars = models.IntegerField(default=5)
    movieid=models.IntegerField()# Assuming 5-star rating system

    def __str__(self):
        return f"{self.description[:50]}..."