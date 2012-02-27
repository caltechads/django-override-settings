# vim: set fileencoding=utf8:
from django.db import models

class Article(models.Model):
    """A models which dynamically installed with ``override_settings``"""
    title = models.CharField('title', max_length=100)
    body = models.TextField('body')
