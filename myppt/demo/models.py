from django.db import models

# Create your models here.

class Ppt(models.Model):
    pid = models.IntegerField(verbose_name='pptid')
    png = models.CharField(max_length=200, verbose_name='url')

    class Meta:
        db_table = 'ppt'

