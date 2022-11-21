from django.db import models

# Create your models here.


class Ads(models.Model):
    ad_image = models.ImageField(upload_to='media', verbose_name='Фото')
    ad_client = models.CharField(max_length=20, verbose_name='Имя клиента')
    ad_discription = models.CharField(
        max_length=200, verbose_name='Описания реклама')
    ad_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    ad_social = models.CharField(max_length=20, verbose_name='Соц. сети')
    ad_dt = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='Время')

    def __str__(self):
        return self.ad_client

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'
