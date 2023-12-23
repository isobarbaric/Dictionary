from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label='Enter a word here', max_length=50)
