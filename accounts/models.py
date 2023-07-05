from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='media/images')
    
    # def image(self):
    #     if self.image
