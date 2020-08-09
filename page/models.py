from django.db import models

# Create your models here.
class Collect(models.Model):
    word=models.CharField(max_length=200)
    mean=models.CharField(max_length=200)


# 웹에 적은 word 요청
#def __str__(self):
#    return self.word 