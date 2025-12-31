import numpy as np

views = [120, 340, 560, 430, 290]
views_array = np.array(views)

print(views_array)
print(type(views_array))

print("차원:", views_array.ndim)
print("형태:", views_array.shape)
print("데이터 타입:", views_array.dtype)

print("표준편차:", np.std(views_array))
print("분산:", np.var(views_array))
