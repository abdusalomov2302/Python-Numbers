from num2words import num2words
a=float(input("pul miqdorini kiriting($): "))

k_en=num2words(a)
n_ru=num2words(a,lang='ru')
umumiy=a
b=a//50
a=a%50
print("$50 talik: ",b,"ta")

c=a//10
a=a%10
print("$10 talik: ",c,"ta")

d=a//5
a=a%5
print("$5 talik: ",d,"ta")

e=a//1
a=a%1
print("$1 talik: ",e,"ta")

print(f"Umumiy summa: ${umumiy}(",(f"{k_en},{n_ru})"))

