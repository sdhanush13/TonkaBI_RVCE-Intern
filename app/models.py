from django.db import models

# Create your models here.
class Insurance(models.Model):
    At='AUTO'
    hlth='HEALTH'
    trm='TERM'
    policy_choices=(
        (At,'Auto'),
        (hlth,'Health'),
        (trm,'TERM'),
    )
    name=models.CharField(max_length=30)
    policy_type=models.CharField(max_length=30,choices=policy_choices,default=At)
    sum_insured=models.FloatField()
    premium=models.FloatField()
    dob=models.DateField()
