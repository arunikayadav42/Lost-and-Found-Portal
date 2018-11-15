from django.db import models
from django_comments_xtd.models import XtdComment
# Create your models here


class MyComment(XtdComment):
	title = models.CharField(max_length=512)
