for i in range(1,51):
    with open(str(i)+"주차.txt",'w',encoding='utf8') as report:
        report.write("-"+str(i)+"주차 주간보고 -\n이름 :\n부서 :\n업무요약 : ")
        
