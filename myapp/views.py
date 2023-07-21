from django.shortcuts import render,redirect
from django.views.generic import View
from django import forms
from myapp.models import Cakes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages


class CakeForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "shape":forms.Select(attrs={"class":"form-select"}),
            "layer":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "cake_pic":forms.FileInput(attrs={"class":"form-control"})
        }
class RegistratinForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }  

#cake login form

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))              


class CakeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm   
        return render(request,"cake-add.html",{"forms":form}) 
    def post(self,request,*args,**kwargs):
        form=CakeForm(request.POST,files=request.FILES)
        if form.is_valid():
           print(form.cleaned_data)
           Cakes.objects.create(**form.cleaned_data)
           messages.success(request,"cake added successfully")
           return redirect("cake-list")
        messages.error(request,"failed")
        return render(request,"cake-add.html",{"form":form})

class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Cakes.objects.all()
        return render(request,"cake-list.html",{"cakes":qs})    
        
class CakeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("ps")
        qs=Cakes.objects.get(id=id)
        return render(request,"cake-detail.html",{"cake":qs}) 

class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("ps")
        qs=Cakes.objects.get(id=id).delete()
        messages.success(request,"cake has been removed successfully")
        return redirect("cake-list")    
           

class CakeEditview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("ps")
        ck=Cakes.objects.get(id=id)
        form=CakeForm(instance=ck)

        return render(request,"cake-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
          id=kwargs.get("ps")
          emp=Cakes.objects.get(id=id)
          form=CakeForm(instance=emp,data=request.POST,files=request.FILES)

          if form.is_valid():
            form.save()
            messages.success(request,"edited successfully")
            return redirect("cake-detail",ps=id)
          messages.error(request,"failed")
          return render(request,"cake-edit.html",{"form":form})


#registration 

class SignUpview(View):
    def get(self,request,*args,**kwargs):
        form=RegistratinForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistratinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created successfully")
            return redirect("signin")
        messages.error(request,"failed")
        return render(request,"register.html",{"form":form})
    
#login

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login scuccessfully")
                return redirect("cake-list")
        messages.error(request,"failed to login")    
        return render(request,"login.html",{"form":form})
    
#logout

def signoutview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


