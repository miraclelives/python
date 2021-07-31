def std_weight(height,gender):
    if gender=="여성":
        standard=height*height*21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100,round(standard,2)))
    else:
        standard=height*height*22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100,round(standard,2)))
  
    
std_weight(1.75,"남자")
