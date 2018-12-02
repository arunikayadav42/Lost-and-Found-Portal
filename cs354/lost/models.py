from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


class Lost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    date_item_lost = models.DateTimeField(default=timezone.now)
    date_item_registered = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)
    found_status = models.CharField(max_length=2, default='NF')  
    # NF means not found

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lost_detail', args=[str(self.pk)])