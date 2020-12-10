from django.shortcuts import render,redirect
from app.models import Insurance
from app.forms import  AddInsurance
from django.views.generic import TemplateView
# Create your views here.
def addInsuranceView(request):
    if request.POST:
        form = AddInsurance(request.POST, request.FILES)
        val = request.POST.get(form.name)
        print("==========================",val,"=================")
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddInsurance()
    return render(request, 'home.html', {'form': form})
class homepageview(TemplateView):
    template_name='home.html'