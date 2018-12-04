from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class Lost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.TextField()
    brand = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_item_lost = models.DateTimeField(default=timezone.now)
    date_item_registered = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)
    item_found = models.BooleanField(default=False)
    claimed_user = models.TextField(null=True)
    # NF means not found

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lost_detail', args=[str(self.pk)])

    # def create_profile(sender, **kwargs  #     if kwargs["created"]:
#         user_profile = UserProfile.objects.create(user=kwargs["instance"])


#   post_save.connect(create_profile, sender=get_user_model())


class Comment(models.Model):
    lost = models.ForeignKey(Lost, on_delete=models.CASCADE, 
                             related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
                               related_name="lost_author")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE, 
                              related_name='replies')
    # approved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('lost_detail', args=[str(self.pk)])

    def __str__(self):
        return self.lost.title

