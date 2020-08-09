from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=80,default="")
    phone =models.CharField(max_length=13,default="")
    description =models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name