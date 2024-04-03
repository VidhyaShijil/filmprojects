from django.db import models

# Create your models here.
class Filmproject(models.Model):
    
    name=models.CharField(max_length=250)
    desc=models.TextField()
    actor=models.TextField()
    date=models.TextField()
    link=models.TextField()
    category=models.TextField()
    year=models.IntegerField()
    userid=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    # def addmovie(self):
    #     name=models.CharField(max_length=250)
    #     desc=models.TextField()
    #     actor=models.TextField()
    #     date=models.TextField()
    #     link=models.TextField()
    #     category=models.TextField()
    #     year=models.IntegerField()
    #     userid=models.IntegerField()
    #     img=models.ImageField(upload_to='gallery')

    # def register(self):
    #     username =models.TextField()
    #     firstname=models.TextField()
    #     lastname=models.TextField()
    #     email=models.TextField()
    #     passwrd=models.TextField()
        

    def __str__(self):
        return self.name
