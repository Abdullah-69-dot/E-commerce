from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order  # يجب أن يكون داخل Meta
        fields = ["full_name", "email", "address"]  # الحقول المطلوبة
