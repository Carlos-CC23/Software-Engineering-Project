from django import forms
from .models import AppointmentHistory

class AppointmentHistoryForm(forms.ModelForm):
    class Meta:
        model = AppointmentHistory
        fields = ['patient_name', 'discussion_notes']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'discussion_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
