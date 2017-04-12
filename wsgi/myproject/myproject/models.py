from django.db import models

#Common

#Faremer

class FarmerAddress(models.Model):
    hnoblock = models.CharField(max_length=128)
    vilage = models.CharField(max_length=30)
    district = models.CharField(max_length=25, default="Fatehabad")
    state = models.CharField(max_length=25, default="Haryana")
    zip_code = models.CharField(max_length=10, default="125111")

    def __unicode__(self):
        return self.vilage

    def __str__(self):
        return self.vilage


class Farmer (models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobileno  = models.IntegerField()
    address = models.OneToOneField(
        FarmerAddress,
             on_delete=models.CASCADE,
             primary_key=True,
         )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

#ToolProvider on Rent
class TPRentAddress(models.Model):
    hnoblock = models.CharField(max_length=128)
    vilage = models.CharField(max_length=30)
    district = models.CharField(max_length=25, default="Fatehabad")
    state = models.CharField(max_length=25, default="Haryana")
    zip_code = models.CharField(max_length=10, default="125111")

    def __unicode__(self):
        return self.vilage

    def __str__(self):
        return self.vilage


class TPRent (models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobileno  = models.IntegerField()
    address = models.OneToOneField(
        TPRentAddress,
             on_delete=models.CASCADE,
             primary_key=True,
         )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Tool (models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    rateType = models.CharField(max_length=20)
    rate  = models.IntegerField()
    tPRent = models.ForeignKey(TPRent, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

