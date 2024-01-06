from django import forms

class WordForm(forms.Form):
    word = forms.CharField(
        label = False,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder': 'Enter a word here'})
    )
