from django.shortcuts import render
from django.views.generic.base import TemplateView
import datetime
# Create your views here.
def viewData(request):
    if request.POST:
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        insurance_type=request.POST.get('insurance_type')
        insurnace_amt=request.POST.get('insurance_amt')
        dob_list=dob.split()
        print(dob_list)
    return render(request,'index.html')