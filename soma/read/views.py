from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')