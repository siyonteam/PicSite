from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    sub_cat = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True)
    is_sub_cat = models.BooleanField(default=False)
    image = models.ImageField(upload_to='categories')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'       

    def __str__(self) -> str:
        return self.name

class Wallpaper(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="posts")
    title = models.CharField(max_length=200 )
    slug = models.SlugField(max_length=200)
    pic = models.ImageField(upload_to='wallpapers')
    description = models.TextField()
    category = models.ManyToManyField(Category , related_name="posts")
    craeted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return self.title