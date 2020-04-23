from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse
from account.models import Account


class Post(models.Model):
    title = models.CharField(max_length=100 , default='sachin')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #author= models.ForeignKey(Account, on_delete=models.CASCADE)
    #author_id = models.AutoField(primary_key=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
