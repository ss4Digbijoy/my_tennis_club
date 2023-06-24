from django.db import models

# Create your models here.
class imagemodel(models.Model):
    img=models.ImageField(upload_to='users')