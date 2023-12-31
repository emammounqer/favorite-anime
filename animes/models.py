from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("anime_detail", args=[str(self.pk)])
