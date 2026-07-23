# Ek hi interface se alag-alag behaviors represent karna.

def process_checkout(processor: PaymentProcessor, amount: float):
    # System doesn't care if it is stripe or razorpay!
    processor.pay(amount)

process_checkout(RazorpayProcessor(), 500)
process_checkout(StripeProcessor(), 500)