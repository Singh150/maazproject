from django.shortcuts import render,redirect,get_object_or_404
from comment.forms import commentform
from comment.models import comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

def plan(request):
    return render(request,'plan.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    concheck = commentform(request.POST or None)
    if concheck.is_valid():
        concheck.save()
        return redirect("home")
    return render(request,'contact.html',{'cform':concheck})

    

def feedback(request):
    return render(request,'feedback.html')
