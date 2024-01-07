from django.urls import path, include
from .views import home, definition, CustomLoginView

urlpatterns = [
    path('', home, name='home'),
    path('search/<str:search_query>/', definition, name='definition'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls'))
]
