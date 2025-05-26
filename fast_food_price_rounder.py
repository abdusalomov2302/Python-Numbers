from num2words import num2words


m1=float(input("Mahsulot narxini kiriting($) "))
m2=float(input("Mahsulot narxini kiriting($) "))
m3=float(input("Mahsulot narxini kiriting($) "))
y=m1+m2+m3
n=round(y,1)
k=num2words(n,to='currency')
m=num2words(n,lang='ru',to='currency')
print(f"umumiy narx:${n}(",f"{k}"','f"{m})")



