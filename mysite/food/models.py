from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(
        max_length=500, default="https://luigispizzakenosha.com/wp-content/uploads/placeholder.png")

    def __str__(self) -> str:
        return self.item_name
