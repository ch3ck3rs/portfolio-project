
from django.db import models

# Create your models here.


class Goal(models.Model):
    title = models.CharField(max_length=100)
    set_date = models.DateField()
    target_date = models.DateField(blank=True, null=True, default='2020-12-3')
    finished_date = models.DateField(blank=True, null=True, default='2020-12-31')
    image = models.ImageField(upload_to='goals/')
    # tldr = models.CharField(max_length=200)
    body = models.TextField()
    set_back = models.TextField(blank=True, default='')
    Jan = models.TextField(blank=True, default='')
    Feb = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def set_date_pretty(self):
        return self.set_date.strftime('%b %e %Y')

    def target_date_pretty(self):
        return self.target_date.strftime('%b %e %Y')
