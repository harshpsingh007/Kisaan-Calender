from django.db import models

# Create your models here.
class Payment(models.Model):
    order_id = models.CharField(max_length=25,default="")
    name = models.CharField(max_length=80,default="")
        
    def __str__(self):
    	return self.name