# Generated by Django 4.1 on 2022-09-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_port', '0013_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='Floor_number',
            field=models.CharField(default='Ground floor', max_length=15),
        ),
    ]
