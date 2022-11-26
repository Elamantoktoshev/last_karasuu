from django.db import models


class Ads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    discription = models.CharField(max_length=200, default=True)
    number = models.CharField(max_length=20)
    social = models.CharField(max_length=20, default=True)
    dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'
