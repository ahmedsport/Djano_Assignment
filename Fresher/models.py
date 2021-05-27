from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(
        upload_to="images/", default="images/default.png")


# class Privacy(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()

    def get_absolute_url(self):
        return reverse("Fresher:single", args=[self.slug])

    def __str__(self):
        return self.title




class Recipes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(
        upload_to="images/", default="images/default.png")


    def __str__(self):
        return self.title        




        
