from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users_Login
# Create your views here.
def one(request):
    return render(request,'home.html')

def newPage(request):
	ids=request.POST.get("user_nameF")
	pwds=request.POST.get("pwdF")
	emailM=request.POST.get("emailF")
	
	sref=Users_Login(user_name=ids,pwd=pwds,email=emailM)
	sref.save()
	return render(request,'result.html',{"message":"registered"})


