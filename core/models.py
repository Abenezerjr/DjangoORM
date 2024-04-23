from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN='IN',"Indian"
        CHINESE='Ch',"Chinese"
        ITALIAN='IT',"Italian"
        GREEK='GR',"Greek"
        FASTFOOD='FF',"Fast Food"
        OTHER='OT',"Other"
    name=models.CharField(max_length=200)
    website=models.URLField(default='')
    date_opened=models.DateTimeField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    restauranet_type=models.CharField(max_length=2,choices=TypeChoices.choices)


    def __str__(self):
        return self.name

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE ,related_name="ratings")
    rating=models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.rating)


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL,null=True ,related_name='sales')
    income=models.DecimalField(max_digits=10,decimal_places=2)
    datetime=models.DateTimeField(auto_now_add=True)