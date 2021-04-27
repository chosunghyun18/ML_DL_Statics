#need what ? need  to calculate count down mefdia
import numpy as np
from scipy import stats
import math
from collections import Counter



# 평균
def info(a1):
    a2 = a1
    a2.sort()
    print(a2)
    cnt = Counter(a1)
    print(cnt)
    a2l = len(a2)
    print("자료수:" ,a2l)

    meana=round(np.mean(a1),3)
    print("평균값 :", meana)
    sum1 = 0
    for i in a2:
        sum1 = (i-meana)**2 + sum1
    sum1 = round(sum1, 3)

    print(sum1)
##################################
    stdn_1 =  (1/(a2l-1)) *sum1
    print("표준 분산 var(n-1) :",round(stdn_1,3))
    print("표준 편차 1/(n-1) :",round(math.sqrt(round(stdn_1, 3)),3))

    ###중앙값
    print("중앙값 median :", np.median(a1))
    # 표준편차값 분 1/n
    print("n 으로 나눈 모분산 var(n) :", round((np.var(a1)), 3))




# 절사 평귡  20% 30%
def Tmean(a, b):
    print(b, "에 절사 평균 :", stats.trim_mean(a, (b / 2) * 0.01))


##########백분위수
def percentile(arry,b):
    arry.sort()
    print(arry)
    len(arry)
    prob = b
    prob= prob*(1/100)
    nump=prob*len(arry)

    if nump - int(nump) == 0:
        print("정수:")
        nump = int(nump)
        print((arry[nump-1]+arry[nump])/2)

    if nump- int(nump) != 0:
        print("소수 소수 첫1 에서 올")
        nump = math.ceil(nump)
        print(nump)
        print((arry[nump-1]))

####### q3  - q1

def qrange(interq):
    interq.sort()
    print("numbver of arrayt ",len(interq))
    lena = len(interq)
    print("this is array of itq want:", interq)
    # 정수 일때 배열이 짝수 갯수
    if(lena  % 2 != 0  ) :
        p =lena/4
        p= math.ceil(p)
        print(p)
        print(interq[p-1] +interq[p])
        print("IQ1 ",(interq[p-1] +interq[p] )/ 2 )
        print("IQ3 ",(interq[3*p - 1] +interq[3*p] )/ 2 )
        print("IQ3-IQ1",(interq[3*p - 1] +interq[3*p] )/ 2  - ((interq[p-1] +interq[p]) / 2))
        print("중앙값 median :", np.median(interq))
    else :
        print("num of array is even")
        p = (lena+1)/ 4
        p= math.ceil(p)
        print(interq[p-1])
        print("IQ1 ", interq[p-1])
        print("IQ3 ", interq[3*p-1])
        print("this is  range of interq rnage" ,interq[3*p-1]  - interq[p-1])
        print("중앙값 median :", np.median(interq))


count = 0
while(count != 1):
    print("배열을 입력하시오  ex) > 1 2 3 4 5")
    array= list(map(float, input().split()))
    print("번호를 입력하시오:")
    print("1:정보(평균,분산,표준편차,빈도수,중앙값)")
    print("2:절사평균")
    print("3:백분위수 원소찾기")
    print("4:Q3 - Q1")
    print("5:exit program")
    num=int(input())
    if num == 1:
        print("1을 선택했음")
        info(array)
    if num == 2 :
        print("2을 선택했음 절사평균")
        print(" put number of p ex) >20 >30 ")
        pnum = int(input( ))
        Tmean(array,pnum)

    if num ==3 :
        print("3을 선택했음 백분위수를 구한다 몊백분위수인가?")
        print("백분위수 입력 ex) 20 ")
        pnum = int(input())
        percentile(array,pnum)

    if num ==4 :
        print("4을 선택했음")
        print("Q3 -Q1")
        qrange(array)

    if num == 5 :
        print("end program")
        count = 1

















