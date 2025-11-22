from django.db import models

from config.constants import MAX_CHAR_LEN, MAX_PWD_LEN

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=MAX_CHAR_LEN)
    last_name = models.CharField(max_length=MAX_CHAR_LEN, null=True, blank=True)
    username = models.CharField(max_length=MAX_CHAR_LEN)
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=MAX_PWD_LEN)
