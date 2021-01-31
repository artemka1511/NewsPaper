from django.contrib.auth.models import User
from django.db import models

article = 'AR'
news = 'NE'

TYPE_NEWS = [(article, 'Статья'), (news, 'Новость')]


class Category(models.Model):
    category_title = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.category_title


class Post(models.Model):
    post_author = models.ForeignKey('accounts.Author', on_delete=models.CASCADE)
    post_choice = models.CharField(max_length=2, choices=TYPE_NEWS, default=article)
    post_datetime_create = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=60, unique=True)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def preview(self):
        self.post_text = self.post_text[:124] + '...'
        return self.post_text

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return self.post_title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_datetime_create = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return self.comment_text



