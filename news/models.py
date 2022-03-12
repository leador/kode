from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse_lazy
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=120, blank=True,
                            unique=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='news_author',
                               on_delete=models.PROTECT)
    poster = CloudinaryField('image')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='get_news')
    tags = models.ManyToManyField('Tag', related_name='get_news')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={"news_slug": self.slug})

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={"tag_slug": self.slug})

    class Meta:
        ordering = ['id']


class Advertise(models.Model):
    company = models.CharField(max_length=60)
    media = CloudinaryField('adv')
    redirect_url = models.URLField()
    click = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.company
