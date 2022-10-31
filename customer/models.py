from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = RichTextUploadingField(blank=True)
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now=True)  # 작성시 자동으로 날짜 설정
    mdate = models.DateTimeField(null=True, blank=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    contents = RichTextUploadingField()
    cdate = models.DateTimeField(auto_now=True)
