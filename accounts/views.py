from django.contrib.auth import authenticate
from django.contrib.auth import	get_user_model
from django.contrib.auth import	login
from django.contrib.auth import	logout

from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def login_view(request):
	print(request.user.is_authenticated)
	title="Login"
	form= UserLoginForm(request.POST or None)
	if form.is_valid():
		username= form.cleaned_data.get("username")
		password= form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated)
		context={"type":"login_form"}
		return redirect("/shops/")

	return render(request, "shops/home_page.html",{"title":title,"form":form,"type":"login_form1"})

def register_view(request):
	title="Register"
	form =UserRegisterForm(request.POST or None)
	if form.is_valid():
		user= form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect("/shops/")

	return render(request, "shops/home_page.html",{"title":title,"form":form,"type":"login_form1"})

def logout_view(request):
	logout(request)
	return redirect("/")

