# Data (attributes) aur unpar kaam karne wale methods ko ek unit (class) mein bind karna, aur internal state ko direct modify hone se rokna.

# Problem: Agar koi parking lot ki total spaces ko directly modify kar de, toh system crash ho jayega.

# Python Reality: Python mein true private variables nahi hote (_ ya __ use hote hain), 
# lekin encapsulation ka matlab hai ki state change hamesha methods ke zariye honi chahiye.

class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance #protected convention

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def get_balance(self)-> float:
        return self._balance