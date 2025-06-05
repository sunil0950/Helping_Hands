from django.db import models

# Create your models here.
class Details(models.Model):
    uid=models.IntegerField(primary_key=True)
    name = models.TextField(max_length=30)
    password = models.TextField(max_length=30)
    cnfpassword = models.TextField(max_length=30)
    phoneno = models.BigIntegerField()
    gender = models.TextField()
    lang = models.TextField()
    state = models.TextField()
    city = models.TextField()
    group = models.TextField()

