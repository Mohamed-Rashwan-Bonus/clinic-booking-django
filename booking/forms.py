from django import forms
from .models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','phone','specialty','date','notes']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'الاسم بالكامل'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'01001234567','dir':'ltr'}),
            'specialty': forms.Select(attrs={'class':'form-select'}),
            'date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'notes': forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'اشرح باختصار (اختياري)'}),
        }
