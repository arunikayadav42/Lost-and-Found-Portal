from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.text import slugify
# Create your models here.


class CustomUser(AbstractUser):
    roll_no = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
    addressline1 = models.TextField()
    addressline2 = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures/users/', null=True,
                                blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.roll_no)
        super(CustomUser, self).save(*args, **kwargs)

<<<<<<< HEAD
=======
    def get_profile(self):
        return reverse("profile_detail", kwargs={'slug': self.slug})
# def create_profile(sender, **kwargs  #     if kwargs["created"]:
#         user_profile = UserProfile.objects.create(user=kwargs["instance"])

>>>>>>> Links for comments working

# # post_save.connect(create_profile, sender=get_user_model())
# from django.db.models.signals import post_save
