from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    sub_cat = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True)
    is_sub_cat = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Wallpaper(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    pic = models.ImageField(upload_to='wallpapers')
    description = models.TextField()
    category = models.ManyToManyField(Category)