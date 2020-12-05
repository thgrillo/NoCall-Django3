from django.db import models



# Create your models here.

class Mark(models.Model):

    empname = models.CharField(max_length=50, default="")
    tecname = models.CharField(max_length=50, default="")
    locname = models.CharField(max_length=50, default="")
    opsticket = models.CharField(max_length=10, default="")
    inorout = models.CharField(max_length=10, default="")
    created_date = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=50, default="")
    longitude = models.CharField(max_length=50, default="")

    # def publish(self):
    #     self.created_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.opsticket