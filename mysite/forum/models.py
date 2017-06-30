from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, verbose_name="商品名")
    content = models.TextField(verbose_name="商品说明")
    created_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(verbose_name="价格", max_digits=20, decimal_places=2)

class Reply(models.Model):
    post = models.ForeignKey('Post', related_name='replies', related_query_name='reply')
    author = models.ForeignKey('auth.User')
    content = models.TextField(verbose_name="内容", default = "")
    created_at = models.DateTimeField(default=timezone.now)
