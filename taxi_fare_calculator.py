from num2words import num2words


a=3.00
c=1.20
b=float(input("masofani kiriting(km): "))
d=round((a+b*c),2)
k=num2words(d,to='currency')
n=num2words(d,lang='ru',to='currency')
print(f"Taxi narxi: ${d}(",f"{k},{n})")

