from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    up_cat = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='sub_cats')
    is_sub_cat = models.BooleanField(default=False)
    image = models.ImageField(upload_to='categories')
    craeted = models.DateField(auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'       

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("pictures:category_detail", kwargs={"category_slug": self.slug,})
class Picture(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="pics")
    title = models.CharField(max_length=200 )
    slug = models.SlugField(max_length=200)
    pic = models.ImageField(upload_to='pictures')
    description = models.TextField()
    category = models.ForeignKey(Category ,on_delete=models.CASCADE ,related_name="pics")
    tags = TaggableManager()
    craeted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("pictures:picture_detail", kwargs={"pk": self.pk,})
    