# Generated by Django 4.1 on 2022-09-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_port', '0015_alter_site_agreement_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='Agreement_duration',
            field=models.CharField(default='No', max_length=15),
        ),
    ]
