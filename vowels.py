s=input()
vowels="aeiouAEIOU"
v=0
for i in s:
    if(i in vowels):
        v+=1
print(v)