from django.db import models


# Create your models here.

class Samsung(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=30)

    class Meta:
        db_table = 'Samsung'

    def __str__(self):
        return self.model


class Xiomi(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=30)

    class Meta:
        db_table = 'Xiomi'

    def __str__(self):
        return self.model
