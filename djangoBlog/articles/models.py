from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later
    def __str__(self):
        return self.title

    def snippet(self): #displays up to first 150 characters of the article
        if len(self.body) > 150:
            return self.body[:150] + '...'
        else:
            return self.body[:150]
