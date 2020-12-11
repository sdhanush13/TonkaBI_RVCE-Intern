import datetime

from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def HomePageView(request):
    to_be_paid = 0
    insuranace_amt = 0
    name = None
    dob = None
    if request.POST:
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        insurance_type = request.POST.get('insurance_type')
        insuranace_amt = int(request.POST.get('insurance_amt'))
        dob_list = dob.split('-')
        birth_date = int(dob_list[0])
        today = datetime.datetime.now()
        date_now = int(today.year)
        age = date_now - birth_date
        if age <= 24:
            return render(request, 'index.html', {'message': "Age must be above 24"})
        else:
            if insurance_type == "auto" and age in range(25, 36):
                to_be_paid = insuranace_amt * 0.03
            elif insurance_type == "health" and age in range(25, 36):
                to_be_paid = insuranace_amt * 0.08
            elif insurance_type == "term" and age in range(25, 36):
                to_be_paid = insuranace_amt * 0.002
            elif insurance_type == "health" and age in range(36, 46):
                to_be_paid = insuranace_amt * 0.11
    return render(request, 'index.html', {'to_be_paid': to_be_paid, 'name': name, 'dob': dob, 'insuranace_amt': insuranace_amt})
