from django import forms
from .models import expense_model

class expense_forms(forms.ModelForm):
    class Meta:
        model=expense_model
        fields='__all__'