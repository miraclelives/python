from random import *
index=0
for i in range(1,51):
    usedtime=randint(5,50)
    os="blank"
    if 5<=usedtime<=15:
        os="o"
        index+=1
    else:
        os=" "
    print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(os,i,usedtime))

print("총 탑승 승객 :",index,"분")
