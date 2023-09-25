import numpy as np
v1 = [[1, 2, 3],
      [3, 4, 5],
      [7, 8, 9]]
v2 = [[10, 20, 30],
      [40, 50, 60],
      [70, 80, 90]]

v3 = [(v1[i] + v2[i] for i in range(len(v1)))]
print(v3)