import datetime
import os.path

from django.db import models


# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = str(timeNow) + str(old_filename)
    return os.path.join('static/assets/img/uploads', filename)


class Property(models.Model):
    address = models.CharField(max_length=500)
    rent = models.IntegerField()
    deposit = models.IntegerField()
    maintenance = models.IntegerField()
    phone = models.IntegerField()
    mail = models.CharField(max_length=50)
    uid = models.IntegerField()
    in_img = models.ImageField(upload_to=filepath, null=True)
    out_img = models.ImageField(upload_to=filepath, null=True)


class NewsLetter(models.Model):
    news_mail = models.CharField(max_length=50)
