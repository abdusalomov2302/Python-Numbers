from num2words import num2words


a=float(input("oy boshidagi ko'rsatkich(kWh): "))
b=float(input("oy oxiridagi ko'rsatkich(kWh): "))
c=0.45
t=round(((b-a)*c),2)
k=num2words(t,to='currency')
n=num2words(t,lang='ru',to='currency')
print(f"to'lov: {t}(",(f"{k},{n})"))

