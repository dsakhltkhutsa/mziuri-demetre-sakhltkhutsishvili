# 1.
class BankAccount:
    max_deposit = 2500
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > self.max_deposit:
            print("shetanili tanxa maqsmalurs gadascda")
        elif amount > 0:
            self.balance += amount
            print(f"angarishze dagericxat {amount} lari", f"angarishze gaqvt {self.balance} lari")
        else:
            print("tanxa unda iyos dadebiti")
    def withdraw(self, amount):
        if amount <= 0:
            print("tanxa unda iyos dadebiti")

        elif amount > self.balance:
            print(f"tqven arasakmarisi tanxa gaqvt {self.balance} lari", f"itxovt {amount} laris gamotanas")
        else:
            self.balance -= amount
            print(f"tqven gamoitanet {amount} lari", f"angarishze gaqvt {self.balance} lari")

    def display_balance(self):
        print(f"mflobeli: {self.owner}")
        print(f"balansi: {self.balance}₾")
acc = BankAccount("demetre saxltxucishvili", 1000)
acc.display_balance()
acc.deposit(100)
acc.deposit(2500)
acc.deposit(2600)
acc.deposit(-100)
acc.deposit(0)

acc.withdraw(-500)
acc.withdraw(2500)
acc.withdraw(5100)
acc.withdraw(200)
acc.withdraw(0)
# 2.
import math
class Shape:
    def describe(self):
        print("i am a shape")
class Polygon(Shape):
    def __init__(self, *sides):
        self.sides = sides
    def describe(self):
        super().describe()
        print(f"I am a polygon with {len(self.sides)} sides: {list(self.sides)}")
class Triangle(Polygon):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(f"{a}, {b}, {c}  ar qmnian samkutxeds")
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    def calc_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2)

t = Triangle(3, 4, 5)
t.describe()
print(f"fartobi: {t.calc_area()}kv. erteuli")





