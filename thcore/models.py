from django.db import models



# Create your models here.

class Mark(models.Model):
    
    tecname = models.CharField(max_length=50, default="")
    locname = models.CharField(max_length=50, default="")
    opsticket = models.CharField(max_length=10, default="19191919")
    created_date = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=50, default="")
    longitude = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.opsticket