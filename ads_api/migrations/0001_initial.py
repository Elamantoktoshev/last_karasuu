# Generated by Django 4.1.3 on 2022-11-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('ad_client', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('ad_discription', models.CharField(max_length=200, verbose_name='Описания реклама')),
                ('ad_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('ad_social', models.CharField(max_length=20, verbose_name='Соц. сети')),
                ('ad_dt', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
