from django import forms
from .models import Receipt
class NewTopicForm(forms.ModelForm):
    message=forms.CharField(widget=forms.TextInput)
    class Meta:
        model=Receipt
        fields= ['total_price']
    pass