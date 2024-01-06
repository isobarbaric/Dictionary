from django.shortcuts import render, redirect
from .word import Word
from .forms import WordForm

def home(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            print(word)
            return redirect('definition', search_query = word)
    else:
        form = WordForm()
 
    return render(request, 'dictionary/base.html', {'form': form})
    # what is an invalid request??
    # deal with invalid request?

def definition(request, search_query):
    current_word = Word(search_query)
    print(search_query)
    if current_word.meanings is None:
        return render(request, 'dictionary/error.html', {'form': WordForm()})
    else:
        return render(request, 'dictionary/result.html', {'search_query' : current_word, 'form': WordForm()})