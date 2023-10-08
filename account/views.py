from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status



class Registerview(APIView):

    def post(self,request):
        try:
            data=request.data
            serializers=RegisterSerializers(data=data)
            if not serializers.is_valid():
                return Response({
                    "error":serializers.errors ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
            

            serializers.save()
            return Response(
                {
                    'data':{},
                     "message":"Accounts created sccessfully"
                },status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({
                    "data":{},
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
        


class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializers=LoginSerializers(data=data)  
            if not serializers.is_valid():
                return Response({
                    "error":serializers.errors ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
            res=serializers.get_jwt_token(serializers.data)
            return Response(res,status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                      "data":{},
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)


