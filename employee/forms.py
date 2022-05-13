# forms.py 
from django import forms 
from .models import Employee
  
class EmployeeForm(forms.ModelForm): 
  
    class Meta: 
        model = Employee
        fields = ['UPLOAD_SKIN_IMAGES','First_Name','Last_Name','Patient_Id']
