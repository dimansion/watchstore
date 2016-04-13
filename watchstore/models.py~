from django.db import models

class Men(models.Model):
    image = models.ImageField (upload_to="images/",null=True,blank=True)
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200, null=True,blank=True)
    STYLE_CHOICES = (
        ('Casual', 'Casual'),
        ('Sporty', 'Sporty'),
    )
    style = models.CharField(max_length=10, choices=STYLE_CHOICES)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

