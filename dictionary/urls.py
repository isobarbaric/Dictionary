from django.urls import path
from .views import home, definition

urlpatterns = [
    path('', home, name='home'),
    path('<str:search_query>/', definition, name='definition')
]
