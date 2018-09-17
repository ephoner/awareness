from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='文章标题', null=False)
    author = models.CharField(max_length=150, verbose_name='文章作者', null=True)
    source = models.CharField(max_length=150, verbose_name='文章来源', null=True)
    content = RichTextField(verbose_name="文章内容", null=False)

    order_index = models.PositiveIntegerField(default=3000)
    category = models.ForeignKey("Category", null=True, on_delete=False)
    tags = models.ManyToManyField("Tag", null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def get_absolute_url(self):
        return reverse("article", kwargs={"pid": self.id})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default="cate")
    description = models.CharField(max_length=5000)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'



    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(default="tag")
    description = models.CharField(max_length=1000)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})

    def __str__(self):
        return self.tag


class Symptom(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True, blank=True)


