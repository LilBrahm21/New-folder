#Brahm Brar, Notes Python

nums= [11,4,43,6,78,3,2]

for num in nums:
    print (num)

    #while loop
x=0

while x <10 :
    print(x)
    x+=1

nums= [1,2,3,4,5,6,7,8,9]
siblings = ["alex","katie", "anderw", "vienna", "tia"]
print(nums)
print(siblings[3])
siblings[7] = "jake"
siblings.pop(5)
siblings.insert(1,"jay")
siblings.insert(2,["alex", "kate","noah"])
print(siblings)

for sibling in siblings:
    print(sibling)

for x in range (1,232,20):
    print(x)
x=1
while x <=20:
    print(x)
    x+=1
import random
x=1
goose - random.randint(1,20)

while x <=20:
    if x ==goose:
    print("goose")
    break
else :
    print("duck")

    x+=1