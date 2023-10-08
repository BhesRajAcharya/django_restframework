from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *

# Create your views here.
class BlogView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
   
    def get(self,request):
       try:
           blog=Blog.objects.filter(user=request.user)
           serializers=BlogSerializers(blog,many=True)
           return Response(
             {
                    'data':serializers.data,
                     "message":"Blogs fetched sccessfully"
                },status=status.HTTP_201_CREATED
           )
       except Exception as e:
            print(e)
            return Response({
           
                    "data":{},
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
          
            


      

     
    def post(self,request):
     try:
       data=request.data
       data['user']=request.user.id
       serializers=BlogSerializers(data=data)
       if not serializers.is_valid():
         return Response({
           
                    "error":serializers.errors ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
       
       serializers.save()

            
         
       return Response(
         {
                    'data':serializers.data,
                     "message":"Blogs created sccessfully"
                },status=status.HTTP_201_CREATED
       )
     except Exception as e:
       print(e)
       return Response({
           
                    "data":{} ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
     



    def patch(self,request):
        
      try:  
        data=request.data
        blog=Blog.objects.filter(uid=data.get('uid'))

        if not blog.exists():
           return Response({
           
                    "data":{} ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
        if request.user!=blog[0].user:
           return Response({
           
                    "data":{} ,
                     "message":"you are not authorized to this blog"},status=status.HTTP_400_BAD_REQUEST)
        
        serializers=BlogSerializers(blog[0],data=data,partial=True)
        if not serializers.is_valid():
           return Response({
           
                    "error":serializers.errors ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
        
        serializers.save()
           


        return Response(
             {
                    'data':serializers.data,
                     "message":"Blogs fetched sccessfully"
                },status=status.HTTP_201_CREATED
           )
      except Exception as e:
        print(e)
         
        return Response(
             {
                    'data':{},
                     "message":"exception occured"
                },status=status.HTTP_400_BAD_REQUEST)
      

    def delete(self,request):
       try:  
        data=request.data
        blog=Blog.objects.filter(uid=data.get('uid'))

        if not blog.exists():
           return Response({
           
                    "data":{} ,
                     "message":"sometthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
        if request.user!=blog[0].user:
           return Response({
           
                    "data":{} ,
                     "message":"you are not authorized to this blog"},status=status.HTTP_400_BAD_REQUEST)
        
        blog[0].delete()
        
        return Response(
             {
                    'data':{},
                     "message":"Blogs deleted sccessfully"
                },status=status.HTTP_201_CREATED)
       
       except Exception as e:
          print(e)
          return Response({
           
                    "data":{} ,
                     "message":"exception occured"},status=status.HTTP_400_BAD_REQUEST)


       
         

           