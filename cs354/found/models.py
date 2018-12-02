from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


class Found(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.TextField()
    brand = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_item_found = models.DateTimeField(default=timezone.now)
    date_item_registered = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('found_detail', args=[str(self.pk)])


class Comment(models.Model):
    found = models.ForeignKey(Found, on_delete=models.CASCADE, 
                              related_name="found_comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
                               related_name="found_author")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE, 
                              related_name='found_replies')
    # approved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('found_detail', args=[str(self.pk)])

    def __str__(self):
        return self.found.title

