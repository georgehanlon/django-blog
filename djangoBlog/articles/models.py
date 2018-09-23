from django.db import models

# Create your models here.
class Article(models.Model):
    title
    slug
    body
    date
    # add in thumbnail later
