from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .word import Word
from .forms import WordForm

# adding search_bar to the login page by overriding the get_context_data method
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # adding search bar to login page
        context['search_bar'] = WordForm()

        # renaming login form
        context['login_form'] = context.pop('form')
        return context

def home(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            print(word)
            return redirect('definition', search_query = word)
    else:
        form = WordForm()
 
    return render(request, 'dictionary/base.html', {'search_bar': form})
    # what is an invalid request??
    # deal with invalid request?

def definition(request, search_query):
    current_word = Word(search_query)
    print(search_query)
    if current_word.meanings is None:
        return render(request, 'dictionary/error.html', {'search_bar': WordForm()})
    else:
        return render(request, 'dictionary/result.html', {'search_query' : current_word, 'search_bar': WordForm()})