#어떤 과정을 거치면 우리 동네 인구구조와 가장 비슷한 지역을 찾을 수 있을까?
#1) 계획대로 한 번에 완성되는 경우는 아주 아주 드물다.
#2) 일단 가장 기본적인 부분(minimal viable product)부터 작게 만들어보고 점점 확대시켜나가는 것이 일반적
#3) tral & error 을 보며 실력을 키움
import csv
f= open("age.csv", encoding = "cp949")
data = csv.reader(f)

result=[]
for row in data:
    if "능동" in row[0]:
        for i in range(3,len(row)):
            result.append(int(row[i]))

import matplotlib.pyplot as plt
plt.plot(result)
plt.show()