from num2words import num2words
from decimal import Decimal,  getcontext


h1=float(input("1 kun xarajatlari:"))
h2=float(input("2 kun xarajatlari:"))
h3=float(input("3 kun xarajatlari:"))
h4=float(input("4 kun xarajatlari:"))
h5=float(input("5 kun xarajatlari:"))
h6=float(input("6 kun xarajatlari:"))
h7=float(input("7 kun xarajatlari:"))
u=round((h1+h2+h3+h4+h5+h6+h7)/7,2)
k=num2words(u,to='currency')
n=num2words(u,lang='ru',to='currency')

print(f"o'rtacha harajat: ${u}(",f"{k},{n})")