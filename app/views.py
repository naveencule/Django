from django.shortcuts import render

# Create your views here.


def function(request):
    return render(request, 'index.html')



def another_function(request):
    return render(request, 'another.html')  