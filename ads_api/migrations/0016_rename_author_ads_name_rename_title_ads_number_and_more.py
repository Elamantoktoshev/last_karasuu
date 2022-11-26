# Generated by Django 4.1.3 on 2022-11-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_api', '0015_ads_delete_adskarasuu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='author',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='title',
            new_name='number',
        ),
        migrations.AddField(
            model_name='ads',
            name='discription',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ads',
            name='dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='social',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
