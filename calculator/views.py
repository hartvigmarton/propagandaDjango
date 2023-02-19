from django.shortcuts import render
from django.http import HttpResponse
from .forms import  PropagandaForm
def say_hello(request):
    return render(request,"index.html",{"name":"Márton"})
# Create your views here.
def test_szevasz(request):
    return render(request,"test.html",{"name":"sfgd"})

def printRequest(request):
    return render(request,"index.html",{"name":"name"})


def home():
    return  render("test.html")


def index(request):
    form = PropagandaForm()
    if request.method == "POST":
        print(request.POST)
    context = {'form':form}
    return render(request,'test.html',context)