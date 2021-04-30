from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=66)

    class Meta:
        verbose_name_plural = 'Categorías'


    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    categories = models.ManyToManyField('Category', related_name='posts')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:blog_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=66)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.body
