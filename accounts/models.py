from django.contrib.auth.models import User
from django.db import models
from news.models import Post, Comment


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        posts = Post.objects.filter(post_author=self)
        post_rating = sum([r.post_rating * 3 for r in posts])
        comment_rating = sum([r.comment_rating for r in Comment.objects.filter(comment_user=self.author)])
        all_to_post_comment_rating = sum([r.comment_rating for r in Comment.objects.filter(comment_post__in=posts)])
        self.author_rating = post_rating + comment_rating + all_to_post_comment_rating
        self.save()




