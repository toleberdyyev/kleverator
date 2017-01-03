from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    tagname =  models.CharField(max_length=100)
    def __str__(self):  # __unicode__ on Python 2
        return self.tagname

class Task(models.Model):
    author = models.ForeignKey('auth.User',related_name='task_author')
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    workers = models.ManyToManyField(User,related_name="task_workers")

    def __str__(self):
        return self.title

    def tagBytag(self):
        array = self.tags.split(",")
        for ar in array:
            if(ar==''):
                array.remove(ar)
        return array

    def givemetags(self):
        print(self.tags)
        return self.tags

