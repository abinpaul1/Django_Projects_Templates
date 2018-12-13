from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    #additional stuff

    portfolia_link = models.URLField(blank=True)

    pro_pic = models.ImageField(upload_to='profile',blank=True)

    def __str__(self):
        return self.user.username
