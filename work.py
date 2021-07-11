from random import *
listA=list(range(1,21))
shuffle(listA)
listB=sample(listA,4)
print("---당첨자 발표---")
print("치킨 당첨자:", listB[0])
print("커피 당첨자:", listB[1:4]) 
print("---축하합니다---")
