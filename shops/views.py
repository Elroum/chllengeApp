from django.shortcuts import render, redirect
from .models import shop_model2
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
#HOME VIEW
def home(request):
	print("home")
	context={"type":"home"}
	return render(request, "shops/home_page.html",context)

#SHOPS VIEW
#I will work on nearby shops here
def shops(request):

	if request.user.is_active :
		print("home")
		table_likes={}
		s=shop_model2.objects.all()
		for x in s:
			if not x.likes.filter(id=request.user.id).exists():
				is_likd=True
			else :
				is_likd=False
			table_likes[x]=is_likd
		context={"shoops":table_likes,"type":"shops"}
		return render(request, "shops/home_page.html",context)
	else:
		print("not logged")
		return redirect('/')

def like_shop(request,id):
	#s_id=request.POST.get('shop_id') 
	is_liked=False
	sho=get_object_or_404(shop_model2, id=id)
	if not sho.likes.filter(id=request.user.id).exists():
		
		sho.likes.add(request.user)

	else:
		sho.likes.remove(request.user.id)

	#print(is_liked)
	return HttpResponseRedirect('/shops/')






