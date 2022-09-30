
from email.policy import default
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os
# Create your models here.ss

class ArticleSeries(models.Model):
    def image_upload_to(self,instance=None):
        if instance:
            return os.path.join("ArticleSeries",slugify(self.slug),instance)
        return None
    title =  models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,default='',blank=True)
    slug = models.SlugField("Series Slug", null=False,blank=False,unique=True)
    published = models.DateTimeField ('Date Published',default=timezone.now)
    author = models.ForeignKey(get_user_model(),default=1,on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/8.jpg',upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return self.title
    class Meta:
        app_label="essesntials"
        verbose_name_plural = 'Series'
        ordering = ['-published']
class Article(models.Model):
    def image_upload_to(self,instance=None):
        if instance:
            return os.path.join("Article",slugify(self.article_slug),instance)
        return None
    title =  models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,default='',blank=True)
    article_slug = models.SlugField("Article Slug", null=False,blank=False,unique=True)
    content = models.TextField(default="")
    notes=HTMLField(blank=True,default="")
    published = models.DateTimeField ('Date Published',default=timezone.now)
    modified =  models.DateTimeField('Date modified',default=timezone.now)
    series= models.ForeignKey(ArticleSeries,default='',verbose_name='Series',on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(),default=1,on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/8.jpg',upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return self.title
    @property
    def slug(self):
        return self.slug + "/"+ self.article_slug
    class Meta:
        app_label="essesntials"
        verbose_name_plural = ' Article'
        ordering = ['-published']