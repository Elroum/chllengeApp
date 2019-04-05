from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth import	get_user_model
from django.contrib.auth import	login
from django.contrib.auth import	logout

#LOGIN  FORM

User = get_user_model()

class UserLoginForm(forms.Form):
	username= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

#Validation for user form
	def clean(self, *args, **kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		user= authenticate(username=username, password=password)
		if username and password:
			user= authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("User or Password not correct")
			#if not user.check_password(password):
			#	raise forms.ValidationError("Incorrect password")

			#if not user.is_active:
			#	raise forms.ValidationError("This user in not longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

#Registration FORM

class UserRegisterForm(forms.ModelForm):
	email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))	
	email_conf= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Email'}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	username= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	class Meta:
		model= User
		fields=[
			'username',
			'email_conf',
			'email',
			'password'
		]

# Validation script for email
	def clean_email(self):
		email= self.cleaned_data.get('email')
		email_conf= self.cleaned_data.get('email_conf')
		if email!= email_conf:
			raise forms.ValidationError("Emails must match")
		email_qs= User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registred")
		return email