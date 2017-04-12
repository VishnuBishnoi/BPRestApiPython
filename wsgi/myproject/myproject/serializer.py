
from rest_framework import serializers
from .models import Farmer, FarmerAddress,TPRentAddress,TPRent,Tool

#Common


#Farmer
class FarmerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmerAddress
        field = ('pk','district','vilage','hnoblock','zip_code','state')

class FarmerSerializer(serializers.ModelSerializer):
    address = FarmerAddressSerializer()

    class Meta:
        model = Farmer
        field = ('pk','name','address','mobileno','password')

#ToolProvider on Rent

class TPRentAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = TPRentAddress
        field = ('pk', 'district', 'vilage', 'hnoblock', 'zip_code', 'state')

class TPRentSerializer(serializers.ModelSerializer):
    address = TPRentAddressSerializer()

    class Meta:
        model = TPRent
        field = ('pk','name','address','mobileno','password')


class ToolSerializer(serializers.ModelSerializer):
    tPRent = TPRentSerializer()

    class Meta:
        model = Tool
        field = ('pk','name','category','rateType','rate','tPRent')

