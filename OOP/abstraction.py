# User ko bas kya ho raha hai dikhana, kaise ho raha hai hiding details.

# LLD Requirement: Machine coding mein interviewer bolega, "Payment Gateway support karo (Razorpay, Stripe, Paytm)". 
# Tumhara core system ko matlab nahi hona chahiye ki payment kaise ho rahi hai, bas pay(amount) call hona chahiye.

# Python mein Abstraction achieve karne ke liye hum abc (Abstract Base Classes) module use karte hain:

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class RazorpayProcessor(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        #Razorpay API call logic
        print(f"Paid {amount} via Razorpay")
        return True

class StripeProcessor(PaymentProcessor):
    def pay(self, amount: float)-> bool:
        # Stripe API call logic
        print(f"Paid {amount} via Stripe")
        return True