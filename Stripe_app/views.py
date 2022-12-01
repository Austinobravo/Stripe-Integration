from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
class StripePayment(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'stripe.html')

    def post(self, request, *args, **kwargs):
        if request.POST.get('submit') =="stripe":
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    # 'name': 'T-shirt',
                    # 'description': 'Comfortable cotton t-shirt',
                    # 'images': ['https://example.com/t-shirt.png'],
                    # 'amount': 2000,
                    # 'currency': 'usd',
                    'price_data': {
                    'currency': 'usd',
                    'unit_amount': 2000,
                    'product_data': {
                        'name': 'T-shirt',
                        'description': 'Comfortable cotton t-shirt',
                        'images': ['https://example.com/t-shirt.png'],
                    },
                    },
                    'quantity': 5,
                }],
                mode='payment',
                success_url=settings.BASE_URL + '/success/',#This is the page it goes to if your payment is successful.
                cancel_url=settings.BASE_URL + '/cancel/',#This is the page it goes to if your payment is unsuccessful.
                
                )

            return redirect(checkout_session.url) 