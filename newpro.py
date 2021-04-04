site= "https://youtube.com"
my_site=site[8:-4]
password= my_site[:3] + str(len(my_site)) + str(my_site.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(site, password))

#위가 내가 만든것 밑은 해답 참조
site= "https://youtube.com"
my_site =site.replace("https://","")
my_site = my_site[:my_site.index(".")]
password= my_site[:3] + str(len(my_site)) + str(my_site.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(site, password))