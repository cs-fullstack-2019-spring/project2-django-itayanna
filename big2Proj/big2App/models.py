from django.db import models
from django.utils import dates
from django.contrib.auth.models import User

# Create your models here.

class NewEntry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=80000)
    dateCreated = models.DateField( null=True, default='')
    lastUpdate = models.DateField(null=True, blank=True)
    authour = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class AddRelatedContent(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=80000)
    dateCreated = models.DateField( null=True, default='')
    lastUpdate= models.DateField(null=True, blank=True)
    parentPost = models.ForeignKey(NewEntry, on_delete=models.SET_NULL, null=True, blank=True)


class AuthorAccount(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(default='')
    password = models.CharField(max_length=200)
    confirm = models.CharField(max_length=200)

