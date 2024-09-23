from django.db import models
from django.core.validators import MinValueValidator



class News(models.Model):
    name = models.CharField(
        max_length=260,
        unique=True,
    )
    description = models.TextField()
    publication_date = models.DateField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:]} {self.publication_date}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()