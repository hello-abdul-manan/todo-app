from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'completed', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter todo title'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter description', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }
