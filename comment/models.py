from django.db import models
from blogs.models import Blog
# Create your models here.


class Comment(models.Model):

    publisher = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.content} by {self.publisher}'

    class Meta:
        ordering = ['created_on']
