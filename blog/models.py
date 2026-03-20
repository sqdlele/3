from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ArticleView(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_views')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['article', 'user'],
                condition=Q(user__isnull=False),
                name='unique_article_user_view',
            ),
            models.UniqueConstraint(
                fields=['article', 'session_key'],
                condition=Q(session_key__isnull=False),
                name='unique_article_session_view',
            ),
        ]

    def __str__(self):
        viewer = self.user.username if self.user else self.session_key
        return f'{self.article_id}:{viewer}'
