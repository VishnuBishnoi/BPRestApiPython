
from django.http import HttpResponse
from .models import Farmer , TPRent ,Tool
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FarmerSerializer,TPRentSerializer,ToolSerializer


"""
def getfarmers(request):
    all_farmers =  Farmer.objects.all()
    return HttpResponse(all_farmers)
"""
# farmer/
class FarmerList(APIView):

    def get(self,request):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#ToolProvider on Rent
class TPRentList(APIView):

    def get(self,request):
        tPRentrs = TPRent.objects.all()
        serializer = TPRentSerializer(tPRentrs, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ToolList(APIView):

    def get(self,request):
        toolList = Tool.objects.all()
        serializer = ToolSerializer(toolList, many=True)
        return Response(serializer.data)

    def post(self):
        pass
