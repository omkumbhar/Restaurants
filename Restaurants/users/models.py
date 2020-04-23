from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from PIL import Image
from account.models import Account

class Profile(models.Model):
    #account = models.OneToOneField(Account , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
