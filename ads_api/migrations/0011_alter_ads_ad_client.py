# Generated by Django 4.1.3 on 2022-11-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_api', '0010_alter_ads_ad_client_alter_ads_ad_discription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ad_client',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
