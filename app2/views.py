from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
def viewData(request):
    if request.POST:
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        print(dob)
    return render(request,'index.html')