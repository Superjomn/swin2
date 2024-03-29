from django.db import models

class HtmlInfo(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    date = models.DateField()

class HtmlSource(models.Model):
    source = models.TextField()
    parsed_source = models.TextField()
    info = models.ForeignKey(HtmlInfo)
