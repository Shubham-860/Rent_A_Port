# Generated by Django 4.0.6 on 2022-07-24 07:00

from django.db import migrations, models
import rent_a_port.models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_port', '0008_remove_property_out_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='out_img',
            field=models.ImageField(null=True, upload_to=rent_a_port.models.filepath),
        ),
    ]
