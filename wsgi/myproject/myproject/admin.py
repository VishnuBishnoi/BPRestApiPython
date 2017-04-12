from django.contrib import admin
from .models import Farmer,FarmerAddress,TPRentAddress,TPRent,Tool

#Common


#Farmer
admin.site.register(FarmerAddress)
admin.site.register(Farmer)

#ToolProvider on Rent
admin.site.register(TPRentAddress)
admin.site.register(TPRent)
admin.site.register(Tool)

