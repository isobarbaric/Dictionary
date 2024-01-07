from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.ModLoginView.as_view(), name='login'),
    path('log-out/', views.log_out, name='log_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('home', views.home, name='home'),
    path('search/<str:search_query>/', views.definition, name='definition'),
    path('add-term/', views.add_term, name='add_term'),
    path('', include('django.contrib.auth.urls'))
]
