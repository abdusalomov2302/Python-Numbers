
from num2words import num2words


a=5.00
c=0.80
b=float(input("masofani kiriting(km): "))
d=round((a+b*c),2)
k=num2words(d,to='currency')
n=num2words(d,lang='ru',to='currency')
print(f"Yetkazib berish narxi: ${d}(",f"{k},{n})")

