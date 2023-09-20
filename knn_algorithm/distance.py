import numpy as np

np.random.seed(0)

dimension = 2
x = np.random.randint(-5, 6, (dimension,))
y = np.random.randint(-5, 6, (dimension,))
print(x, y)

# Euclidean Distance
euclidean_distance = x - y  # 원소별 뺄셈
print(euclidean_distance)
euclidean_distance = euclidean_distance ** 2
print(euclidean_distance)
euclidean_distance = np.sum(euclidean_distance)
print(euclidean_distance)
euclidean_distance = np.sqrt(euclidean_distance)
print(euclidean_distance)

# Euclidean Distance 정리 :
euclidean_distance = np.sqrt(sum((x - y) ** 2))
print(euclidean_distance)

# Manhattan Distance
manhattan_distance = x - y
print(manhattan_distance)
manhattan_distance = np.abs(manhattan_distance)
print(manhattan_distance)
manhattan_distance = sum(manhattan_distance)
print(manhattan_distance)

# Manhattan Distance 정리 :
manhattan_distance = np.sum(abs(x - y))
print(manhattan_distance)
