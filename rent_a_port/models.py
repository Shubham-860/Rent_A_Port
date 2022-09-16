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
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.address


class Appointment(models.Model):
    owner_id = models.IntegerField()
    appointment_date_time = models.DateTimeField()
    message = models.CharField(max_length=500)
    user_id = models.IntegerField()


class Site(models.Model):
    # validation
    show = models.BooleanField(default=False)

    # ID
    uid = models.IntegerField()

    # Location of the property
    address = models.CharField(max_length=500)
    Message = models.CharField(max_length=500, default="Empty")

    # General information
    rent = models.IntegerField()
    deposit = models.IntegerField()
    maintenance = models.IntegerField()
    BHK = models.CharField(max_length=15, default="1 BHK")
    Floor_number = models.CharField(max_length=10, default="Ground floor")
    Pet_allowed = models.CharField(max_length=15, default="No")
    Parking = models.CharField(max_length=15, default="Yes")
    Property_type = models.CharField(max_length=15, default="House")
    Posted_by = models.CharField(max_length=15, default="House")
    Agreement_duration = models.CharField(max_length=15, default="No")
    Electricity_water = models.CharField(max_length=15, default="No")
    Available_from = models.DateField()
    Posted_on = models.DateTimeField(auto_now_add=True)

    # Contact details
    phone = models.IntegerField()
    mail = models.CharField(max_length=50)

    # Images
    in_img = models.ImageField(upload_to=filepath, null=True)
    out_img = models.ImageField(upload_to=filepath, null=True)

    def __str__(self):
        return self.address


class NewsLetter(models.Model):
    news_mail = models.CharField(max_length=50)

    def __str__(self):
        return self.news_mail
