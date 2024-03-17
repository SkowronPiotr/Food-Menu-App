from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(
        max_length=500, default="https://luigispizzakenosha.com/wp-content/uploads/placeholder.png")

    def __str__(self) -> str:
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
