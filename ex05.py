import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("numpy 버전 : ", np.__version__)
  # -> 출력(numpy 버전 :  2.4.0)
print("pandas 버전 : ",pd.__version__)
  # -> 출력(pandas 버전 :  2.3.3)
num_list = [1,2,3,4,5]
data = np.array(num_list)

print(num_list)  # 출력 -> [1, 2, 3, 4, 5]
print(data)  # 출력 -> [1 2 3 4 5]

####################
print(max(num_list))
print(data.max())
print(max(data))
# -> 출력시 3가지 모두 5 출력
# max, min, sum 모두

####################
print(data.mean())
# -> mean(평균값) 은 np방식에서만 사용 가능