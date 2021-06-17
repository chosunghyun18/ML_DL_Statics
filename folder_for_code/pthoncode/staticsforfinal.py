




###################### 소수 4에서 반올 필요!!
import math


# 이항 분 포   n , p , x
def binomaldistiribution(n,p,x):
    N = []
    for i in range(n):
        N.append(i+1)

    combi1 = combinations(N,x)
    #f(x)
    o=list(combi1)
    one =len(o)
    result = one*(p**x)*((1-p)**(n-x))
    return result



def factorial(inp):
    result = inp
    i = inp
    while i > 1:
        i -= 1
        result *= i
    if result == 0:
        result = 1
    return result

def poisson(inp1, inp2, inp3):
    mean = inp1 * inp2
    result = ((math.exp(-mean)) * (mean ** inp3)) / factorial(inp3)
    return result

#초기 하분포
from itertools import combinations
# 초기 하분포
def Hypergeo(N,M,k,x):
    n= []
    for i in range(N):
        n.append(i+1)
    m= []
    for i in range(M):
        m.append(i+1)

    P=N-M
    p=[]
    for i in range(P):
        p.append(i+1)

    combi1 = combinations(m,x)
    combi2 = combinations(p,k-x)
    combi3 = combinations(n,k)

    #f(x)
    one=list(combi1)
    two=list(combi2)
    three=list(combi3)

    want_x=(len(one)*len(two))/len(three)
    print("p(x=a):",round(want_x,6))


###############################################################################################

print("this is 이항 분포")
n,p,x = 6,0.4,3
print(round(binomaldistiribution(n,p,x),6))
n,p,x = 4,0.6,3
print(round(binomaldistiribution(n,p,x),6))
n,p,x = 4,0.6,4
print(round(binomaldistiribution(n,p,x),6))

print("")


#초기하분포
print("---this is 초기하분포-----")

N=10    #총수 신발 30     # 10
M=3      #특성 불량 5   # 여자 7
k=6     #뽑은거 표본         #6명 추출
x=2      #궁금한값 x=a      # 2명?
a=Hypergeo(N,M,k,x)
print("-----------------------------------")

#이항 포아송
# inp1 : 시행횟수, 평균 회수                          # 매달 3 번 일어남 다음달 5번 확률?
# inp2 : ,요구하는회수.시간                               #n=3,p=1,,x=5
# inp3 : 사상 발생 횟수                   # 1 시간에 3번 울림 15분간 중에 울릴 확률 /////   n=3 , p=0.25 , x=0 후에 1 -p
print("--------------")
print("this is 포아송")

n,p,x= 1,1,1
print(round(poisson(n,p,x),6))
n,p,x=80,0.5,0
print(round(poisson(n,p,x),6))
n,p,x=6,1,8
print(round(poisson(n,p,x),6))



print("---------------------------------")



# 지수 분포  exponential distribute
t=2     # 요구하느 시간
l=2   # 평균수
lt=l*t
print("------------------")
print("지수분포")
print("p(x>=a):",round(math.exp(-lt),5))
print("p(x<=a):",1-round(math.exp(-lt),5))

# 정규 분포 계산
########### Z
print("------------------")     # s = 표준편차!!!    N(m,s^2)
print("------------------")
m,s,x = 20,4,14.5


print("z is ",(x-m)/s)










