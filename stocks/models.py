from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name