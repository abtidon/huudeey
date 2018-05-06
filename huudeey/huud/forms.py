

from django import forms
<<<<<<< HEAD
from django.contrib.admin.widgets  import AdminDateWidget
from django.contrib.admin  import  widgets
import datetime
from bootstrap_datepicker.widgets import DatePicker
=======
import datetime
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
from .models import Prodsale

class saledateform(forms.Form):
    prodname  = forms.CharField(label='Product Name', max_length=100)
    class Meda:
       model = Prodsale
       fields = ['prodname']




<<<<<<< HEAD
class searchcostform(forms.Form):
    unitcost  = forms.FloatField(label='Unit Cost')
    class Meda:
       model = Prodsale
       fields = ['unitcost']



class searchdateform(forms.ModelForm):
       fdate = forms.DateField(help_text="Enter From Date as YYYY-MM-DD  ")
       edate = forms.DateField(help_text="Enter End Date  as YYYY-MM-DD  ")
       class Meta:
         model = Prodsale
         fields = ['saledate']



        
            


    
=======
class searchdateform(forms.Form):
    saledate  = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    class Meda:
       model = Prodsale
       fields = ['saledate']

class searchcostform(forms.Form):
    unitcost  = forms.DateField(label='Unit Cost')
    class Meda:
       model = Prodsale
       fields = ['saledate']
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
