from django.urls import path
from .views import BasePageView, HomePageView, AboutPageView

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),  # Set base as the index
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
