from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Enquiry
from .forms import EnquiryForm

# Create your views here.
def welcome(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def contribute(request):
    form = EnquiryForm(request.POST,request.FILES)
    if request.method == 'POST': 
        if form.is_valid():
            enquiry = form.save()
            enquiry.save()
            print("Message succesfully sent!")
    else:
        form = EnquiryForm()
    return render(request,'contribute.html',{"form":form})