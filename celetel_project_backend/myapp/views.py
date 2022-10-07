from django.shortcuts import render
from django.http import HttpResponse
from myapp.serializers import signup_serializers
from myapp.models import signup
from rest_framework.renderers import JSONRenderer,json
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
class url(APIView):
  def get(self,request):
    data=signup.objects.all().values()

    res=list(data)
   
    return Response(res)
class signupdata(APIView):

#  {
#         "id": 1,
#         "name": "akhil",
    #         "email": "akhil1234jainth@gmail.com",
    #         "username": "akhil00744",
    #         "password": "akhil"
    #     }
 def post(self,request,format=None):
   if request.method=="POST":
    json_data=request.data


    serializer=signup_serializers(data=request.data)


    if serializer.is_valid():
        serializer.save()
        return Response({'Successfully inserted'})
    
    else:
         return Response(status=500)
   
   

class login(APIView):

 def post(self,request,format=None):
   if request.method=="POST":
    json_data=request.data
    def func(json_data):
      if signup.objects.filter(username=json_data['username']).filter(password=json_data['password']).values():
        return True
      else:
        False
    a=func(json_data)
    if a==True:
       return Response({'Login Successfully'})
    else:
         return Response(status=500)
      
   
   

class forgetpass(APIView):

 def put(self,request,format=None):
   if request.method=="PUT":
    json_data=request.data
    def func(json_data):
      if signup.objects.filter(email=json_data['email']).values():
        return True
      else:
        False
    a=func(json_data)
    if a==True:
     
     a1=signup.objects.filter(email=json_data['email']).first()
     a1.password=json_data['password']
     a1.save()
     return Response({'Successfully new password created'})

    else:
         return Response(status=500)

     
    
        
   

class reset_pass(APIView):

 def put(self,request,format=None):
   if request.method=="PUT":
    json_data=request.data
    def func(json_data):
      if signup.objects.filter(username=json_data['username']).filter(password=json_data['current_password']).values():
        return True
      else:
        False
    a=func(json_data)
    if a==True:
     
     a1=signup.objects.filter(username=json_data['username']).first()
     a1.password=json_data['new_password']
     a1.save()
     return Response({'Successfully new password created'},status=200)
    else:
         return Response(status=500)

      

   
        
   

