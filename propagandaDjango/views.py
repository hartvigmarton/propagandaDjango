from django.shortcuts import render
from calculator.forms import NameForm, PropagandaForm
from django.http import HttpResponseRedirect

def say_bye(request):
    return render(request,"index.html",{"name":"Márton"})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'test.html', {'form': form})

def index(request):
    form = PropagandaForm()
    if request.method == "POST":
        print(request.POST)
    if request.method == "GET":
        print("hello")
    context = {'form':form}
    return render(request,'index.html',context)