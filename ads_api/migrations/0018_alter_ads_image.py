# Generated by Django 4.1.3 on 2022-11-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_api', '0017_ads_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
    ]