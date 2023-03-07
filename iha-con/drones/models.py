from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=100,null=True)
    slug = models.SlugField(max_length=100,null=True)
    def __str__(self):
        return self.categoryName


class Drone(models.Model):
    brand = models.CharField(max_length=100,verbose_name="marka")
    model = models.CharField(max_length=50,verbose_name="model")
    weight = models.FloatField()
    image = models.ImageField(upload_to="drones/%Y/%m/%d/",default="drones/indir.jpeg",verbose_name="fotoğraf")
    avaliable = models.BooleanField(default=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.model