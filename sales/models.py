from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


def articles_image_path(instance, filename):
    # MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    return f'user_{instance.pk}/{filename}'


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pcode = models.CharField(max_length=10)
    pname = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="images/", blank=True)
    unitprice = models.IntegerField()
    discountrate = models.DecimalField(max_digits=11, decimal_places=2)
    description = RichTextUploadingField(blank=True, null=True)
    create_date = models.DateTimeField(null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pcode + " " + self.pname + " " + str(self.unitprice) + " " + str(self.discountrate)
