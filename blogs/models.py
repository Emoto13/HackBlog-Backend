from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.title}  - {self.content[:50]}... "


class PoliticsBlog(Blog):
    pass


class SportBlog(Blog):
    pass


class OpinionBlog(Blog):
    pass


class TechBlog(Blog):
    pass


class OtherBlog(Blog):
    pass
