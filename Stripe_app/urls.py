from django.urls import path
from .views import *

urlpatterns=[
    path('payment/stripe', StripePayment.as_view(), name="stripepayment"),
]
#Change the myview to your view function in your views.py file