
class Ticket:
    def __init__(self, name, price, amount, language="Geo"):
        self.name = name
        self.price = price
        self.amount = amount
        self.language = language

    def __str__(self):
        return self.name, self.price, self.amount, self.language

    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.amount > other.amount
        return self.amount > other
    def __lt__(self, other):
        if isinstance(other, Ticket):
            return self.amount < other.amount
        return self.amount < other
    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.amount == other.amount
        return self.amount == other

class User:
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance
    def __str__(self):
        return self.user_name, self.balance

    def deposit(self, money):
        self.balance += money
        print(f"balansi sheivso {money}larit. axali balansi: {self.balance}lari")

    def buy(self, ticket, amount):
        cost = ticket.price * amount
        if ticket.amount < amount:
            print(f"{ticket.movie}ze marto {ticket.amount}biletebia darchenili")
        if self.balance < cost:
            print(f"arasakmarisi tanxa. sawiroa {cost}lari, balanszea {self.balance}lari")
        self.balance -= cost
        ticket.amount -= amount
        print(f"tqven iyidet {amount} bileti filmze {ticket.movie}. "
              f"daxarjet: {cost}lari. balansze dagrchat: {self.balance}lari")

