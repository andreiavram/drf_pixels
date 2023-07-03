from django.contrib.auth import get_user_model
from django.db import models


class ColorBox(models.Model):
    color = models.CharField(max_length=6)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

