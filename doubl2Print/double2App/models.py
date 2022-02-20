from django.db import models


# Create your models here.
class Product(models.Model):
    pro_image = models.ImageField(upload_to='pro-img')
    pro_title = models.CharField(max_length=250)
    pro_desc = models.TextField()

    def __str__(self):
        return self.pro_title

class Canvas(models.Model):
    canva_img = models.ImageField(upload_to='canva-img')
    canva_title = models.CharField(max_length=250)
    canva_desc = models.TextField()
