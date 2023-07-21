from django.db import models

# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=250)
    flavour=models.CharField(max_length=200)
    options=(
        ("round","round"),
        ("square","square"),
        ("heart","heart")
    )
    shape=models.CharField(max_length=200,choices=options,default="round",null=True,blank=True)
    layer=models.CharField(max_length=200) 
    description=models.CharField(max_length=2550)
    weight=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    cake_pic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name

