from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'completed', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'rows': 4
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500'
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-emerald-600 focus:ring-emerald-500 border-slate-300 rounded'
            }),
        }
