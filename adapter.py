import decimal
import math


"""
This is an example of the adapter structural pattern implemented in Python.

Scenario:
We have a system that can send payments to multiple external payment gateways
that have differing programming interfaces.  We will implement our own interface
that we will use to always send payments the same way regardless of which gateway
we're sending the payment to.  We will create adapters for each of the external
gateways to make them conform to our unified sending interface.
"""


class Stripe:
    """
    Represents an external programming interface that has a "create_payment"
    method that accepts a value in cents
    """

    def create_payment(self, value: int):
        print("Send payment to stripe:", value)


class AuthorizeNet:
    """
    Represents another external interface that has a "make_payment" method that
    accepts a value as a decimal
    """

    def make_payment(self, value: decimal.Decimal):
        print("Send payment to authorize.net:", value)


class PaymentGatewayAdapter:
    """
    This is our own interface where we'll define how we want to send payments
    regardless of which gateway we're sending them to.

    We'll always use "process_payment" with a decimal value
    """

    def process_payment(self, value: decimal.Decimal):
        raise NotImplementedError


class StripeAdapter(PaymentGatewayAdapter):
    def __init__(self, stripe: Stripe):
        self.stripe = stripe

    def process_payment(self, value: decimal.Decimal):
        value_as_cents = math.ceil(value * 100)
        self.stripe.create_payment(value_as_cents)


class AuthorizeNetAdapter(PaymentGatewayAdapter):
    def __init__(self, authorize_net: AuthorizeNet):
        self.authorize_net = authorize_net

    def process_payment(self, value: decimal.Decimal):
        self.authorize_net.make_payment(value)


stripe = Stripe()
authorize_net = AuthorizeNet()

stripe_adapter = StripeAdapter(stripe)
authorize_net_adapter = AuthorizeNetAdapter(authorize_net)

stripe_adapter.process_payment(19.99)
authorize_net_adapter.process_payment(24.99)
