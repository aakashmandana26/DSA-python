str="RLRLLRRLRL"
dict={}
countR=0
countL=0
finalCount=0
for i in str:
    
    if i=="R":
        countR+=1
    if(i=="L" and countR!=0):
        countL+=1
    if(countL > countR):
        finalCount+=countR
        countR=0
        countL=0
if(countL != 0):
    finalCount += min(countL, countR)

print(finalCount)
    