from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from bridgenet_payment.apps.core.views.complete_payment import CompletePaymentView

app_name = 'core'

urlpatterns = [
    url(r'^login/$',
        LoginView.as_view(template_name="core/login.html"),
        name="login"),
    url(r'^complete_payment/(?P<payment_id>\d+)/$',
        CompletePaymentView.as_view(),
        name="complete-payment"),
    url(r'payment_completed/$',
        TemplateView.as_view(template_name='core/payment_completed.html'),
        name="payment-completed")
]
