from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='文章类名')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'category'
        verbose_name = '文章种类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_timestamp = models.DateTimeField(verbose_name="修改时间")
    excerpt = models.CharField(max_length=250,blank=True,null=True,verbose_name='内容摘要')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='posts',verbose_name="种类")
    tags = models.ManyToManyField('Tag',null=True,blank=True,verbose_name='文章标签')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',verbose_name='作者')

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'post'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

