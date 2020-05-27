from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class FeaturedPost(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()

class