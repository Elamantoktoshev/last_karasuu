# Generated by Django 4.1.3 on 2022-11-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_api', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ad_client',
            field=models.CharField(blank=True, max_length=20, verbose_name='Имя клиента'),
        ),
    ]
