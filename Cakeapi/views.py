# from django.shortcuts import render
# from django.shortcuts import render
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from myapp.models import Cakes
# from rest_framework.decorators import action

# class CakeSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     class Meta:
#         model=Cakes
#         fields="__all__"

# class CakesView(ViewSet):
   
#     def list(self,request,*args,**kwargs):
#         qs=Cakes.objects.all()
#         if "flavour" in request.query_params:
#             flv=request.query_params.get("flavour")
#             qs=qs.filter(flavour__iexact=flv)
#         if "shape" in request.query_params:
#             shape=request.query_params.get("shape")
#             qs=qs.filter(shape__iexact=shape) 
#         if "layer" in request.query_params:
#             lyr=request.query_params.get("layer")
#             qs=qs.filter(layer__iexact=lyr)        
        
#         serializer=CakeSerializer(qs,many=True)
#         return Response(data=serializer.data)
    
#     def create(self,request,*args,**kwargs):
#         serializer=CakeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     def retrieve(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Cakes.objects.get(id=id)
#         serializer=CakeSerializer(qs)
#         return Response(data=serializer.data)
    
#     def update(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         cake_obj=Cakes.objects.get(id=id)
#         serializer=CakeSerializer(instance=cake_obj,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     def destroy(self,request,*args,**kwargs):
#         id=kwargs.get("pk") 
#         try:
#             Cakes.objects.get(id=id).delete()
#             return Response(data="deleted")   
#         except Exception:
#             return Response(data="no matching record found")
        
#     #custome method

#     @action(methods=["get"],detail=False)
#     def flavour(self,request,*args,**kwargs):
#         qs=Cakes.objects.all().values_list("flavour",flat=True).distinct()
#         return Response(data=True)


        



# Create your views here.


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from Cakeapi.serializers import Userserializer,CakeSerializer
from django.contrib.auth.models import User
from myapp.models import Cakes
from rest_framework import authentication,permissions

class UserView(ModelViewSet):
    serializer_class=Userserializer
    queryset=User.objects.all()
    model=User
class CakeView(ModelViewSet):
    serializer_class=CakeSerializer
    queryset=Cakes.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]    
    def create(self, request, *args, **kwargs):
        serializer=CakeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)