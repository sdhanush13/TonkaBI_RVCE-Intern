from django import forms
from app.models import Insurance
from material import *

class AddInsurance(forms.ModelForm):
    name = forms.CharField()
    At='AUTO'
    hlth='HEALTH'
    trm='TERM'
    policy_choices=(
        (At,'Auto'),
        (hlth,'Health'),
        (trm,'TERM'),
    )
    insurance_type=forms.CharField(label='Policy Type',widget=forms.Select(choices=policy_choices))
    sum_insurance = forms.FloatField()
    dob=forms.DateField()
    payable=forms.CharField(disabled=True)

    layout = Layout(Fieldset('Insurance Details',
                             Row('name', 'insurance_type'),
                             Row('sum_insurance'),
                             Row('dob'),
                             Row('payable'), ))

    class Meta:
        model = Insurance
        fields = ('name', 'insurance_type', 'sum_insurance', 'dob', 'payable')
