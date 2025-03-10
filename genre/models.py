from django.db import models
from pkg_resources import require


class Genre(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
