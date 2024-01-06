from django import forms

class WordForm(forms.Form):
    word = forms.CharField(
        max_length = 50,
        label = '',
        widget = forms.TextInput(attrs={'placeholder': 'Enter a word here'})
    )
