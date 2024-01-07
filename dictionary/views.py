from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .word import Word
from .forms import WordForm, RegistrationForm, VocabForm
from .models import VocabTerm

# adding search_bar to the login page by overriding the get_context_data method
class ModLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # adding search bar to login page
        context['search_bar'] = WordForm()

        # renaming login form
        context['login_form'] = context.pop('form')

        return context

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # print("User created:", user)
            login(request, user)
            # print("User authenticated:", request.user.is_authenticated)

            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'search_bar': WordForm(), 'signup_form': form})

@login_required(login_url = '/login/')
def log_out(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            print(word)
            return redirect('definition', search_query = word)
    else:
        form = WordForm()
 
    # print("home:", request.user.is_authenticated)

    if request.user.is_authenticated:
        return render(request, 'dictionary/home.html', {'search_bar': form, 'terms': VocabTerm.objects.filter(user=request.user)})
    else:
        return render(request, 'dictionary/base.html', {'search_bar': form})

@login_required(login_url = '/login/')
def add_term(request, current_word):
    # add term to database, if it doesn't already exist (exception)
    try:
        VocabTerm.objects.create(user = request.user, word = current_word)
    except IntegrityError:
        pass

    # go back to the original search query
    return redirect('definition', search_query = current_word)

def definition(request, search_query):
    current_word = Word(search_query)
    print(search_query)

    if current_word.meanings is None:
        return render(request, 'dictionary/error.html', {'search_bar': WordForm()})
    else:
        # checks if word is already in the user's list
        word_exists = VocabTerm.objects.filter(user=request.user, word=search_query).exists()
        return render(request, 'dictionary/result.html', {'search_query' : current_word, 'search_bar': WordForm(), 'user_list': word_exists})