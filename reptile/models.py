from django.db import models

class HtmlInfo(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    date = models.DateField()

class Html(models.Model):
    content = models.TextField()
    info = models.ForeignKey(HtmlInfo)
