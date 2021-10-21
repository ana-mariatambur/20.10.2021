s=input("s: ")
b=""
c=0
c2=0
ta=""
to=""
snv=list(s)
inv=""
for i in s:
    if i=="A":
        c+=1
    if i!="B":
        b+=i
a=s.replace("A","*")
for x in range(len(s)-1):
    if s[x]+s[x+1]=="MA":
        c2+=1
ta=s.replace("MA","TA")
to=s.replace("TO","")
snv.reverse()
inv="".join(snv)
print(c) #a)
print(a) #b)
print(b) #c)
print(c2) #d)
print(ta) #e)
print(to) #f)
print(inv) #g)