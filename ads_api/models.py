from django.db import models

# Create your models here.


# class Ads(models.Model):
#     id = models.IntegerField(primary_key=True)
#     ad_image = models.ImageField(upload_to='media')
#     ad_client = models.CharField(
#         max_length=20, blank=True, null=False)
#     ad_discription = models.CharField(
#         max_length=200)
#     ad_number = models.CharField(
#         max_length=20)
#     ad_social = models.CharField(
#         max_length=20)
#     ad_dt = models.DateTimeField(
#         auto_now_add=True)

# def __str__(self):
#     return self.ad_client

# class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'Реклама'
#     verbose_name_plural = 'Рекламы'


class AdsKarasuu(models.Model):
    id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    social = models.CharField(max_length=20)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'
