from django.db import models
GENDER_CHOICES = (
   ('M', 'MALE'),
   ('F', 'FEMALE')
)
CHECKIN_CHOICES = (
   ('M', 'MALE'),
   ('F', 'FEMALE')
)
# Create your models here.
class Customer(models.Model):
    uid = models.CharField(max_length=255,primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    phnNo = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES,default="NONE",max_length=128)
    paymentMode = models.CharField(max_length=100)
    regDate = models.DateField( auto_now=True)
    story = models.CharField(max_length=100)
    checkIn =models.CharField(choices=CHECKIN_CHOICES,default="NO",max_length=128)




    def __str__(self):
        return self.uid