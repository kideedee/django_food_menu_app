from django.db import models


# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='data:image/jpeg;base64,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')

