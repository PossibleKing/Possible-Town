n=input("number")
n=int(n)
p=float(input("price"))
if n<2:
    j=1
if n>=2 and n<4:
    j=0.8
if n>+4:
    j=0.6
t=n*p*j
print(t)
