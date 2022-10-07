from django.db import models

# Create your models here.


class Test(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=32)


class Inputs(models.Model):
    input_value = models.IntegerField()


