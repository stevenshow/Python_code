from django.urls import path
from .views import DateView, DateAdd

urlpatterns = [
    path('show/', DateView.as_view()),
    path('add/', DateAdd.as_view())
]
