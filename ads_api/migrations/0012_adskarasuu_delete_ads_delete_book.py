# Generated by Django 4.1.3 on 2022-11-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_api', '0011_alter_ads_ad_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsKarasuu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('social', models.CharField(max_length=20)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Ads',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
