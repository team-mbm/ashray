from django.db import models

# Create your models here.
class name(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class name1(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
