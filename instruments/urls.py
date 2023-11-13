from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('instrument/', views.InstrumentList.as_view()),
    path('instrument/<int:pk>/', views.InstrumentDetail.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)