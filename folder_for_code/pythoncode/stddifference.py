#표준 편차를 구하는데 있어 numpy 와 pandas 의 계산 방식 즉 결과가 다르게 나온다
import numpy as np
from scipy import stats
import math
import pandas as pd


a = [64,64.8,66,63.5,65,68,67,63.6,67.6,68.9]
dfa = pd.DataFrame(a)

np.mean(a)
print(np.std(a))

pandasstd=dfa.std()
print(pandasstd)



""""
1.848350616089924
0    1.948333
dtype: float64
""""


# 소표본을 사용하는데있어 계산식중 n 와 n-1 을 나누는것에 차이 즉 자유도의 개입 차이가 있다.
#위와 같은 계산식은 30 보다 작은 소표본으로 n-1 을 나눈 계산 식을 이용한 pandas 를 사용하는것이 적절하다고 생각이 든다
