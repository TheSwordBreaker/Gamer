from django.db import models

# Create your models here.

class rating(models.Model):
    name    = models.CharField(max_length=50,null=True)
    rating  = models.DecimalField(max_digits=5, decimal_places=1,blank=True)
    des     = models.TextField()
    hasRelease = models.BooleanField()
   
