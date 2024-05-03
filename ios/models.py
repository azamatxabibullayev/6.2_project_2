from django.db import models


# Create your models here.

class Iphone(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=30)

    class Meta:
        db_table = 'Iphone'

    def __str__(self):
        return self.model
