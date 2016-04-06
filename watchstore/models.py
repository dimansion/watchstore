from django.db import models

class Men(models.Model):
    image = models.ImageField (upload_to="images/",null=True,blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

