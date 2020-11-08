from json import loads

from bridgenet_client.client import BridgenetClient
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.views.generic import FormView


class CompletePaymentForm(forms.Form):
    amount = forms.FloatField()


class CompletePaymentView(LoginRequiredMixin, FormView):
    template_name = 'core/complete_payment.html'
    form_class = CompletePaymentForm
    success_url = '/payment_completed/'

    def get_context_data(self, **kwargs):
        client = BridgenetClient()
        response = client.retrieve_payment_details(int(self.kwargs['payment_id']))
        data = loads(response.content)
        kwargs['status'] = data['status']
        kwargs['account_name'] = data['quote_request']['account_name']
        kwargs['amount'] = data['amount']
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        client = BridgenetClient()
        client.capture_payment(int(self.kwargs['payment_id']), form.cleaned_data['amount'])
        return super().form_valid(form)
