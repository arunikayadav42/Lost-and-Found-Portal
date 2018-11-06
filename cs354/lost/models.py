from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


class Lost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    location = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', null=True,
                                blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('lost_detail', args=[str(self.id)])


class Comment(models.Model):
    lost = models.ForeignKey(Lost, on_delete=models.CASCADE, 
                             related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('lost_detail', args=[str(self.id)])

    def __str__(self):
        return self.text