from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Cakes

class Userserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        
class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields="__all__"       